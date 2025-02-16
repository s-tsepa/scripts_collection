import json
import hashlib

RECIEVER = 'max.ivanov@mail.ru'
MESSAGE = 'Я Марк Гилберт, частный адвокат покойного господина Михаила Иванова. Он и его семья погибли в результате несчастного случая без завещания. Теперь банк обратился ко мне как к его частному адвокату, чтобы представить бенефициара. Поскольку у вас одна фамилия, и вы родом из одной страны, я хочу представить ваше имя в банк. Пусть банк перечислит вам сумму в размере 18,5 млн долларов США. Мы будем делить его 50/50. Все юридические формальности будут решаться нашей юридической фирмой. Я получу все законные документы на наследство, для успешного выпуска фонда к вам без каких-либо препятствий. После вашего ответа я дам вам дополнительную информацию и разъяснения по этому бизнесу. В ожидании вашего ответа, искренне ваш, Марк Гилберт Эсквайр'

def sha1(s):
    return hashlib.sha1(s.encode()).hexdigest()

def email_structure(reciever, message, nonce):
    res_dict = dict()
    res_dict['reciever'] = reciever
    res_dict['message'] = message
    res_dict['nonce'] = nonce
    # print(res_dict)

    return json.dumps(res_dict, ensure_ascii=False)


for nonce in range(1, 10 ** 9):
    s = email_structure(RECIEVER, MESSAGE, str(nonce))
    print(sha1(s))

    prefix = s[:5]
    if prefix == '0' * len(prefix):
        exit()
