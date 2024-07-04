from stt_tts import fake_stt_engine, fake_tts_engine
from masking import *
from encryption import AESCipher
from database import create_connection, create_table, insert_data
import datetime

def main():
    # STT Engine
    text = fake_stt_engine('data/sample_text.txt')
    print("Original Text: ", text)

    # Masking
    #masked_text = mask_test_data(text)
    masked_text = mask_sensitive_data(text)
    print("Masked Text1: ", masked_text)

    # Encryption
    aes_cipher = AESCipher('mysecretpassword')
    encrypted_text = aes_cipher.encrypt(masked_text)
    print("Encrypted Text: ", encrypted_text)

    # Database
    connection = create_connection()
    create_table(connection)
    insert_data(connection, '홍길동', str(datetime.date.today()), 30, '서울시 강남구 역삼동 123-45', masked_text, encrypted_text)
    connection.close()

    # TTS Engine
    fake_tts_engine(masked_text)

if __name__ == "__main__":
    main()
