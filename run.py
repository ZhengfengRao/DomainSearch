import urllib2
import json

max_try = 3
error_count = 0
time_out = 20
whoisapi = "http://whomsy.com/api/";
skipped_file = 'skipped.txt'
skipped = set()
pinying = ["a","ai","an","ang","ao","ba","bai","ban","bang","bao","bei","ben","beng","bi","bian","biao","bie","bin","bing","bo","bu","ca","cai","can","cang","cao","ce","ceng","cha","chai","chan","chang","chao","che","chen","cheng","chi","chong","chou","chu","chuai","chuan","chuang","chui","chun","chuo","ci","cong","cou","cu","","cuan","cui","cun","cuo","da","dai","dan","dang","dao","de","deng","di","dian","diao","die","ding","diu","dong","dou","du","duan","dui","dun","duo","e","en","er","fa","fan","fang","fei","fen","feng","fo","fou","fu","ga","gai","gan","gang","gao","ge","gei","gen","geng","gong","gou","gu","gua","guai","guan","guang","gui","gun","guo","ha","hai","han","hang","hao","he","hei","hen","heng","hong","hou","hu","hua","huai","huan","huang","hui","hun","huo","ji","jia","jian","jiang","jiao","jie","jin","jing","jiong","jiu","ju","juan","jue","jun","ka","kai","kan","kang","kao","ke","ken","keng","kong","kou","ku","kua","kuai","kuan","kuang","kui","kun","kuo","la","lai","lan","lang","lao","le","lei","leng","li","lia","lian","liang","liao","lie","lin","ling","liu","long","lou","lu","lv","luan","lue","lun","luo","ma","mai","man","mang","mao","me","mei","men","meng","mi","mian","miao","mie","min","ming","miu","mo","mou","mu","na","nai","nan","nang","nao","ne","nei","nen","neng","ni","nian","niang","niao","nie","nin","ning","niu","nong","nu","nv","nuan","nue","nuo","o","ou","pa","pai","pan","pang","pao","pei","pen","peng","pi","pian","piao","pie","pin","ping","po","pu","qi","qia","qian","qiang","qiao","qie","qin","qing","qiong","qiu","qu","quan","que","qun","ran","rang","rao","re","ren","reng","ri","rong","rou","ru","ruan","rui","run","ruo","sa","sai","san","sang","sao","se","sen","seng","sha","shai","shan","shang","shao","she","shen","sheng","shi","shou","shu","shua","shuai","shuan","shuang","shui","shun","shuo","si","song","sou","su","suan","sui","sun","suo","ta","tai","tan","tang","tao","te","teng","ti","tian","tiao","tie","ting","tong","tou","tu","tuan","tui","tun","tuo","wa","wai","wan","wang","wei","wen","weng","wo","wu","xi","xia","xian","xiang","xiao","xie","xin","xing","xiong","xiu","xu","xuan","xue","xun","ya","yan","yang","yao","ye","yi","yin","ying","yo","yong","you","yu","yuan","yue","yun","za","zai","zan","zang","zao","ze","zei","zen","zeng","zha","zhai","zhan","zhang","zhao","zhe","zhen","zheng","zhi","zhong  ","zhou","zhu","zhua","zhuai","zhuan","zhuang","zhui","zhun","zhuo","zi","zong","zou","zu","zuan","zui","zun","zuo"];

def whois(domain):
    if domain in skipped:
        return
        
    global error_count
    if error_count > max_try:
        print "[exceed max try, exit.]"
        error_count = 0
        return
        
    print "searching "+ domain
    
    try:
		response = urllib2.urlopen(whoisapi+domain, '', time_out);
		data = json.load(response);
		if data["type"] == "success":
			if data["message"] == "NOT FOUND" or data["message"].find("No match for " + domain) >= 0:
				print "**************** avaiable! **************";
				output = open("avaiable.txt", 'w+');
				output.write(domain);
				close(output);
			else:
			    add_skipped(domain)
			    print " registed!";
		error_count = 0
		
    except Exception, e:
        error_count = error_count + 1
        print e
        print "[trying again...]"
        whois(domain)

def add_skipped(domain):
    global skipped
    try:
        skipped.add(domain)
        fd = open(skipped_file, 'a')
        fd.write(domain+'\n')
        fd.close()
    except Exception, e:
        print e
    
def load_skipped():
    global skipped
    try:
        for line in open(skipped_file):
            skipped.add(line.strip('\n'))
    except Exception, e:
        print e
    
def run():
    load_skipped()
    for first in pinying:
        for second in pinying:
            whois(first+second+".com");
			#whois(first+second+".net");
	
run();

