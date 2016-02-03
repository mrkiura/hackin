# from flask import request, Response
# from redis import Redis
# import time
# from datetime import datetime
# from .main import main
# import logging

# redis = Redis()

# ONLINE_LAST_MINUTES = 5


# def mark_online(user_id):
#     now = int(time.time())
#     expires = now + (ONLINE_LAST_MINUTES * 60) + 10
#     all_users_key = 'online-users/%d' % (now // 60)
#     user_key = 'user-activity/%s' % user_id
#     p = redis.pipeline()
#     p.sadd(all_users_key, user_id)
#     p.set(user_key, now)
#     p.expireat(all_users_key, expires)
#     p.expireat(user_key, expires)
#     p.execute()


# def get_user_last_activity(user_id):
#     last_active = redis.get('user-activity/%s' % user_id)
#     if last_active is None:
#         return None
#     return datetime.utcfromtimestamp(int(last_active))


# def get_online_users():
#     current = int(time.time()) // 60
#     minutes = xrange(ONLINE_LAST_MINUTES)
#     return redis.sunion(['online-users/%d' % (current - x)
#                          for x in minutes])


# # @main.before_app_request
# # def mark_current_user_online():
# #     mark_online(request.remote_addr)


# # @main.route('/online')
# # def see_online():
# #     return Response('Online: %s' % ', '.join(get_online_users()),
# #                     mimetype='text/plain')

# # logger = logger = logging.getLogger(__name__)

# # USER_ONLINE_KEY = 'online_user'
# # USER_OFFLINE_KEY = 'offline_user'


# # def get_connection():
# #     '''
# #     Create and return a Redis connection. Returns None on failure.
# #     '''
# #     try:
# #         conn = redis.Redis()
# #         return conn
# #     except redis.RedisError, e:
# #         logger.error(e)

# #     return


# # def poll_users(username):
# #     '''this function is called when a user logs in '''
# #     connection = get_connection()
# #     if connection:
# #         try:
# #             connection.sadd(USER_ONLINE_KEY, username)
# #         except redis.RedisError, e:
# #             logger.error(e)


# # def tick():
# #     '''
# #     Call this function to "age out" the old set by renaming the current set
# #     to the old.
# #     '''
# #     conn = get_connection()
# #     if conn:
# #         try:
# #             conn.rename(USER_ONLINE_KEY, USER_OFFLINE_KEY)
# #         except redis.ResponseError:
# #             try:
# #                 del conn[USER_OFFLINE_KEY]
# #             except redis.RedisError, e:
# #                 logger.error(e)
# #         except redis.RedisError, e:
# #             logger.error(e)


# # def get_users_online():
# #     '''
# #     Returns a set of user names which is the union of the current and old
# #     sets.
# #     '''
# #     conn = get_connection()
# #     if conn:
# #         try:
# #             return conn.isunion([USER_ONLINE_KEY, USER_OFFLINE_KEY])
# #         except redis.RedisError, e:
# #             logger.error(e)
# #     return set()
