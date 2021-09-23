VK_1 = 'vk.com##.post_author,.wall_text:has-text(//{0}//i):upward(.post)'

_VK_OTHER_CSS_CLASSES = ','.join([
    '.audio_row',
    '.fans_idol_row',
    '.group_list_row',
    '.groups_row',
    '.GroupsRecommendationsBlock__listRow',
    '.reply',  # комментарии
    '.video_item',
    '.wall_card_tiny',  # похожие сообщества
])
VK_2 = f'vk.com##{_VK_OTHER_CSS_CLASSES}:has-text(//{{0}}//i)'
YOUTUBE = 'youtube.com###dismissible:has-text(//{0}//i)'
