# coding=utf-8 
# @Time :2018/11/9 20:58
import os
import re
import time

import itchat
from itchat.content import *

msg_dict = {}  # 定义字典存储消息
rev_tmp_dir = "E:\\pycharm\\coding\\Daily_Test\\WeChat\\"  # 定义文件存储临时目录
if not os.path.exists(rev_tmp_dir):
    os.mkdir(rev_tmp_dir)
face_bug = None  # 处理表情解决方法


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO, FRIENDS],
                     isFriendChat=True, isGroupChat=True)
def handler_receive_msg(msg):  # 将接收到的消息存放在字典中，不接受不具有撤回功能的信息
    global face_bug, group_members, group_name, msg_content
    msg_time_rec = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 格式化本地时间戳
    msg_id = msg['MsgId']  # 消息Id
    msg_time = msg['CreateTime']
    if 'ActualNickName' in msg:  # 判断是否为群消息
        from_user = msg['ActualUserName']  # 群消息的发送者，用户的唯一标识
        msg_from = msg['ActualUserName']
        friends = itchat.get_friends(update=True)
        for friend in friends:
            if from_user == friend['UserName']:  # 判断群里撤回消息的是否为自己好友
                if friend['RemarkName']:  # 优先使用好友的备注名称，没有则使用昵称
                    msg_from = friend['RemarkName']
                else:
                    msg_from = friend['NickName']
                break
        groups = itchat.get_chatrooms(update=True)
        for group in groups:
            if msg['FromUserName'] == group['UserName']:  # 根据群消息匹配哪个群
                group_name = group['NickName']
                group_members = group['MemberCount']
                break
        group_name = group_name + ' (' + str(group_members) + ')'
    else:  # 否则输入个人信息
        if itchat.search_friends(userName=msg['FromUserName'])['RemarkName']:
            msg_from = itchat.search_friends(userName=msg['FromUserName'])['RemarkName']
        else:
            msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']
        group_name = ''

    if msg['Type'] in ('Text', 'Friends'):
        msg_content = msg['Text']  # 如果发送的消息是文本或者好友推荐
    elif msg['Type'] in ('Recording', 'Attachment', 'Video', 'Picture'):
        msg_content = r"" + msg['FileName']  # 如果发送的文件是附件，视频，图片和语音
        msg['Text'](rev_tmp_dir + msg['FileName'])  # 保存文件
    elif msg['Type'] == 'Card':
        msg_content = msg['RecommendInfo']['NickName'] + r" 的名片"
    elif msg['Type'] == 'Map':
        x, y, location = re.search(
            "<location x=\"(.*?)\" y=\"(.*?)\".*label =\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度->" + x.__str__() + "经度->" + y.__str__()
        else:
            msg_content = r"" + location
    elif msg['Type'] == 'Sharing':  # 如果消息为分享的音乐或者文章
        msg_content = msg['Text']
    face_bug = msg_content

    # 更新字典
    msg_dict.update({
        msg_id: {
            "msg_from": msg_from,
            "msg_time": msg_time,
            "msg_time_rec": msg_time_rec,
            "msg_type": msg['Type'],
            "msg_content": msg_content,
            "group_name": group_name
        }
    })


# 处理撤回的消息
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
# 收到note通知类消息，判断是不是撤回并进行相应操作
def send_msg_helper(msg):
    global face_bug
    if re.search(r"\<\!\[CDATA\[.*撤回了一条消息\]\]\>", msg['Content']) is not None:
        # 获取消息的ID
        old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>",
                               msg['Content']).group(1)
        old_msg = msg_dict.get(old_msg_id, {})
        if len(old_msg_id) < 11:
            itchat.send_file(rev_tmp_dir + face_bug, toUserName='filehelper')
            os.remove(rev_tmp_dir + face_bug)
        else:
            msg_body = "惊了！！有人撤回消息" + "\n" \
                       + old_msg.get('msg_from') + '撤回了 ' + old_msg.get('msg_type') + "消息" + "\n" \
                       + old_msg.get('msg_time_rec') + '\n' \
                       + "撤回了什么 看下面" + "\n" \
                       + r"" + old_msg.get('msg_content')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
