import re

def mask_name(text):
    # 특정 키워드 다음에 오는 이름 마스킹
    specific_name_pattern = re.compile(r'(고객|이름|성함|고객님|상담원)[:\s]*([가-힣]{2,4})')
    text = specific_name_pattern.sub(lambda x: x.group(1) + ' ' + x.group(2)[0] + '*' * (len(x.group(2)) - 1), text)

    # "제 이름은", "저는", "내 이름은" 등 패턴 인식
    name_intro_pattern = re.compile(r'(제\s*이름은|저는|내\s*이름은)\s*([가-힣]{2,4})')
    text = name_intro_pattern.sub(lambda x: x.group(1) + ' ' + x.group(2)[0] + '*' * (len(x.group(2)) - 1), text)

    # 일반적인 한국 이름 패턴 마스킹 (한 글자의 성 뒤에 두 글자 또는 세 글자가 오는 패턴)
    name_pattern = re.compile(r'\b([가-힣]{1})([가-힣]{2,3})\b')
    text = name_pattern.sub(lambda x: x.group(1) + '*' * len(x.group(2)), text)

    return text

def mask_phone(text):
    # 전화번호 마스킹
    phone_pattern = re.compile(r'(\b\d{2,3})-(\d{3,4})-(\d{4}\b)')
    return phone_pattern.sub(lambda x: x.group(1) + '-' + '*' * len(x.group(2)) + '-' + '*' * len(x.group(3)), text)

def mask_address(text):
    # 주소 마스킹 (시/도 구/군 동/읍/면 패턴)
    address_pattern = re.compile(r'\b([가-힣]+[시도])\s([가-힣]+[구군])\s([가-힣]+[동읍면])\s([가-힣0-9-]+)\b')
    return address_pattern.sub(lambda x: x.group(1) + ' ' + '*' * len(x.group(2)) + ' ' + '*' * len(x.group(3)) + ' ' + x.group(4), text)

def mask_email(text):
    # 이메일 마스킹
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    return email_pattern.sub(lambda x: x.group(0)[0] + '***@***' + x.group(0)[x.group(0).find('.'):], text)

def mask_sensitive_data(text):
    text = mask_phone(text)
    text = mask_address(text)
    text = mask_email(text)
    text = mask_name(text)  # 이름 마스킹을 마지막에 적용하여 다른 마스킹에 영향받지 않게 함
    return text

# 예제 텍스트
sample_text = """
고객: 여보세요, 안녕하세요.
상담원: 네, 안녕하세요 홍길동 고객님 맞으시죠?
고객: 네, 맞습니다.
상담원: 오늘 무엇을 도와드릴까요?
고객: 제가 최근에 카드 사용 내역을 확인하고 싶은데요.
상담원: 네, 고객님. 카드번호를 말씀해 주시겠어요?
고객: 네, 제 카드번호는 1234-5678-9101-1121 입니다.
상담원: 네, 확인해 보겠습니다. 잠시만 기다려 주세요.
고객: 네, 알겠습니다.
상담원: 고객님, 확인되었습니다. 6월 1일부터 6월 30일까지의 사용 내역을 보내드리겠습니다. 주소를 다시 한번 확인해 주시겠어요?
고객: 네, 제 주소는 서울시 강남구 역삼동 123-45 입니다.
상담원: 네, 고객님. 사용 내역은 이메일로 보내드리겠습니다. 이메일 주소는 abc@example.com 맞으시죠?
고객: 네, 맞습니다.
상담원: 알겠습니다. 추가로 다른 문의 사항이 있으신가요?
고객: 아니요, 괜찮습니다. 감사합니다.
상담원: 네, 감사합니다. 좋은 하루 되세요.
고객: 네, 감사합니다. 안녕히 계세요.
"""

masked_text = mask_sensitive_data(sample_text)
print("Masked Text:", masked_text)
