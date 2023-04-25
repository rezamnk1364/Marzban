from collections import deque
import config
from datetime import datetime as dt
from models.admin import Admin
from models.user import UserResponse
from enum import Enum
from typing import Type

from pydantic import BaseModel


queue = deque()


class ActionType(Enum):
    user_created = "user_created"
    user_updated = "user_updated"
    user_deleted = "user_deleted"
    user_limited = "user_limited"
    user_expired = "user_expired"
    user_enabled = "user_enabled"
    user_disabled = "user_disabled"

    hosts_updated = "hosts_updated"


class Notification(BaseModel):
    enqueued_at: float = dt.utcnow().timestamp()
    tries: int = 0


class HostsUpdated(Notification):
    action: ActionType = ActionType.hosts_updated
    by: Admin


class UserNotification(Notification):
    username: str


class UserCreated(UserNotification):
    action: ActionType = ActionType.user_created
    by: Admin
    user: UserResponse


class UserUpdated(UserNotification):
    action: ActionType = ActionType.user_updated
    by: Admin
    user: UserResponse


class UserDeleted(UserNotification):
    action: ActionType = ActionType.user_deleted
    by: Admin


class UserLimited(UserNotification):
    action: ActionType = ActionType.user_limited
    by: Admin
    user: UserResponse


class UserExpired(UserNotification):
    action: ActionType = ActionType.user_expired
    by: Admin
    user: UserResponse


class UserEnabled(UserNotification):
    action: ActionType = ActionType.user_enabled
    by: Admin
    user: UserResponse


class UserDisabled(UserNotification):
    action: ActionType = ActionType.user_disabled
    by: Admin
    user: UserResponse
    reason: str = None


def notify(message: Type[Notification]) -> None:
    if config.WEBHOOK_ADDRESS:
        queue.append(message)
