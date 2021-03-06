"""
Enrollment track related signals.
"""
from __future__ import absolute_import

from django.dispatch import Signal

ENROLLMENT_TRACK_UPDATED = Signal(providing_args=['user', 'course_key'])
UNENROLL_DONE = Signal(providing_args=["course_enrollment", "skip_refund"])
ENROLL_STATUS_CHANGE = Signal(providing_args=["event", "user", "course_id", "mode", "cost", "currency"])
REFUND_ORDER = Signal(providing_args=["course_enrollment"])
SAILTHRU_AUDIT_PURCHASE = Signal(providing_args=["user", "course_id", "mode"])
