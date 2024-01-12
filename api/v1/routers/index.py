from fastapi import APIRouter
from api.v1.routers import party, image, party_action, player, moderator

router = APIRouter()

router.include_router(moderator.router, prefix="/moderator", tags=["V1 - Moderator"])
router.include_router(player.router, prefix="/player", tags=["V1 - Player"])
router.include_router(party_action.router, prefix="/party_action", tags=["V1 - Party_action"])
router.include_router(image.router, prefix="/image", tags=["V1 - Image"])
router.include_router(party.router, prefix="/party", tags=["V1 - Party"])
