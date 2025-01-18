from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy import func

from dependencies import get_db
from domain.schemas.friend_schemas import FriendWithStatisticResponse
from repository.models import Friend, Memory, MemoryFriendMapping

router = APIRouter(
    prefix="/friend",
    tags=["friend"],
)


@router.get(
    "/with-statistic",
    response_model=List[FriendWithStatisticResponse],
    description="친구 목록을 통계 정보와 함께 조회합니다.",
)
def get_friends_with_statistic(
    db: Session = Depends(get_db)
):
    # 친구별 통계를 저장할 리스트
    result = []

    # 모든 친구 정보를 가져옵니다
    friends = db.query(Friend).all()

    for friend in friends:
        # 1. 해당 친구가 언급된 전체 메모리 수를 계산합니다 (total_count)
        total_count = db.query(MemoryFriendMapping).count()

        # 2. 해당 친구가 언급되었으며 feeling이 1인 메모리 수를 계산합니다 (local_count)
        # Memory와 MemoryFriendMapping 테이블을 조인하여 조건에 맞는 케이스를 찾습니다
        local_count = (
            db.query(Memory)
            .join(
                MemoryFriendMapping,
                Memory.id == MemoryFriendMapping.memory_id
            )
            .filter(
                MemoryFriendMapping.friend_id == friend.id,
                Memory.feeling == 1
            )
            .count()
        )

        # 3. 비율을 계산합니다
        # total_count가 0인 경우를 대비하여 예외 처리를 합니다
        ratio = local_count / total_count if total_count > 0 else 0.0

        # 4. 응답 객체를 생성하여 결과 리스트에 추가합니다
        friend_stat = FriendWithStatisticResponse(
            id=friend.id,
            name=friend.name,
            image=friend.photo,
            totalCount=total_count,    # 전체 등장 횟수
            localCount=local_count,    # feeling이 1인 메모리에서의 등장 횟수
            ratio=ratio                # local_count / total_count의 비율
        )
        result.append(friend_stat)

    # 5. ratio를 기준으로 내림차순 정렬합니다
    # 이를 통해 가장 높은 비율을 가진 친구가 먼저 나오게 됩니다
    sorted_result = sorted(result, key=lambda x: x.ratio, reverse=True)

    return sorted_result
