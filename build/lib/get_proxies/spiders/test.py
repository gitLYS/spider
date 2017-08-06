# import mysql.connector
#
# config={
#     'user':'root',
#     'password':'lys',
#     'host':'127.0.0.1',
#     'port':3306,
#     'database':'lys'
# }
#
# conn=mysql.connector.connect(**config)
# cur=conn.cursor()
# try:
#     sql="select ip,port from proxies where flag=1 limit 100"
#     cur.execute(sql)
#     result=cur.fetchall()
#     for i in result:
#             print(i[0]+':'+i[1])
# except Exception as e:
#     print(e)
#     cur.close()
#     conn.close()
# # cur.execute('commit')
# cur.close()
# conn.close()

# sql="insert proxies values('%s','%s',%d,'%s')" % ('111',2,1,'http')
# print(sql)
#



# import json
#
# js='{"data":[{"directors":["邓肯·琼斯"],"rate":"8.3","cover_x":2600,"star":"45","title":"源代码","url":"https:\/\/movie.douban.com\/subject\/3075287\/","casts":["杰克·吉伦哈尔","维拉·法米加","米歇尔·莫纳汉","杰弗里·怀特","拉塞尔·皮特斯"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p988260245.jpg","id":"3075287","cover_y":3851},{"directors":["滕华涛"],"rate":"7.3","cover_x":2143,"star":"40","title":"失恋33天","url":"https:\/\/movie.douban.com\/subject\/4873490\/","casts":["白百何","文章","张嘉译","王耀庆","张子萱"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1252876266.jpg","id":"4873490","cover_y":3000},{"directors":["乔纳森·戴米"],"rate":"8.7","cover_x":2489,"star":"45","title":"沉默的羔羊","url":"https:\/\/movie.douban.com\/subject\/1293544\/","casts":["朱迪·福斯特","安东尼·霍普金斯","斯科特·格伦","安东尼·希尔德","布鲁克·史密斯"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1593414327.jpg","id":"1293544","cover_y":3686},{"directors":["弗朗西斯·福特·科波拉"],"rate":"9.2","cover_x":580,"star":"50","title":"教父","url":"https:\/\/movie.douban.com\/subject\/1291841\/","casts":["马龙·白兰度","阿尔·帕西诺","詹姆斯·肯恩","理查德·卡斯特尔诺","罗伯特·杜瓦尔"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1910907590.jpg","id":"1291841","cover_y":898},{"directors":["戈尔·维宾斯基"],"rate":"8.6","cover_x":1500,"star":"45","title":"加勒比海盗","url":"https:\/\/movie.douban.com\/subject\/1298070\/","casts":["约翰尼·德普","杰弗里·拉什","奥兰多·布鲁姆","凯拉·奈特莉","杰克·达文波特"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1596085504.jpg","id":"1298070","cover_y":2228},{"directors":["朱塞佩·托纳多雷"],"rate":"8.7","cover_x":1201,"star":"45","title":"西西里的美丽传说","url":"https:\/\/movie.douban.com\/subject\/1292402\/","casts":["莫妮卡·贝鲁奇","朱塞佩·苏尔法罗","埃丽萨·莫鲁奇"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p792400696.jpg","id":"1292402","cover_y":1704},{"directors":["宫崎骏"],"rate":"8.9","cover_x":1509,"star":"45","title":"哈尔的移动城堡","url":"https:\/\/movie.douban.com\/subject\/1308807\/","casts":["倍赏千惠子","木村拓哉","美轮明宏","我修院达也","神木隆之介"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2174346180.jpg","id":"1308807","cover_y":2131},{"directors":["皮埃尔·科凡","克里斯·雷纳德"],"rate":"8.5","cover_x":1013,"star":"45","title":"神偷奶爸","url":"https:\/\/movie.douban.com\/subject\/3287562\/","casts":["史蒂夫·卡瑞尔","杰森·席格尔","拉塞尔·布兰德","朱莉·安德鲁斯","威尔·阿奈特"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p792776858.jpg","id":"3287562","cover_y":1500},{"directors":["奥利维埃·纳卡什","埃里克·托莱达诺"],"rate":"9.1","cover_x":2181,"star":"45","title":"触不可及","url":"https:\/\/movie.douban.com\/subject\/6786002\/","casts":["弗朗索瓦·克鲁塞","奥玛·希","安娜·勒尼","奥德雷·弗勒罗","托马·索利韦尔"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1454261925.jpg","id":"6786002","cover_y":3120},{"directors":["宫崎骏"],"rate":"9.0","cover_x":2064,"star":"45","title":"天空之城","url":"https:\/\/movie.douban.com\/subject\/1291583\/","casts":["田中真弓","横泽启子","初井言荣","寺田农","常田富士男"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1446261379.jpg","id":"1291583","cover_y":2933},{"directors":["薛晓路"],"rate":"7.4","cover_x":700,"star":"40","title":"北京遇上西雅图","url":"https:\/\/movie.douban.com\/subject\/10574468\/","casts":["汤唯","吴秀波","海清","宋美曼","宋美慧"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1878328589.jpg","id":"10574468","cover_y":1000},{"directors":["管虎"],"rate":"8.0","cover_x":717,"star":"40","title":"老炮儿","url":"https:\/\/movie.douban.com\/subject\/24751756\/","casts":["冯小刚","许晴","张涵予","刘桦","李易峰"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2292976849.jpg","id":"24751756","cover_y":1000},{"directors":["马丁·斯科塞斯"],"rate":"8.6","cover_x":2480,"star":"45","title":"禁闭岛","url":"https:\/\/movie.douban.com\/subject\/2334904\/","casts":["莱昂纳多·迪卡普里奥","马克·鲁弗洛","本·金斯利","马克斯·冯·叙多夫","米歇尔·威廉姆斯"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1832875827.jpg","id":"2334904","cover_y":3543},{"directors":["柯克·德·米科","克里斯·桑德斯"],"rate":"8.7","cover_x":510,"star":"45","title":"疯狂原始人","url":"https:\/\/movie.douban.com\/subject\/1907966\/","casts":["尼古拉斯·凯奇","瑞恩·雷诺兹","艾玛·斯通","凯瑟琳·基纳","克拉克·杜克"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1867084027.jpg","id":"1907966","cover_y":755},{"directors":["周星驰"],"rate":"6.8","cover_x":3500,"star":"35","title":"美人鱼","url":"https:\/\/movie.douban.com\/subject\/19944106\/","casts":["邓超","罗志祥","张雨绮","林允","徐克"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2316177058.jpg","id":"19944106","cover_y":4889},{"directors":["王家卫"],"rate":"8.6","cover_x":1335,"star":"45","title":"重庆森林","url":"https:\/\/movie.douban.com\/subject\/1291999\/","casts":["林青霞","金城武","梁朝伟","王菲","周嘉玲"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p792381411.jpg","id":"1291999","cover_y":1900},{"directors":["昆汀·塔伦蒂诺"],"rate":"8.7","cover_x":514,"star":"45","title":"低俗小说","url":"https:\/\/movie.douban.com\/subject\/1291832\/","casts":["约翰·特拉沃尔塔","乌玛·瑟曼","阿曼达·普拉莫","蒂姆·罗斯","塞缪尔·杰克逊"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p1910902213.jpg","id":"1291832","cover_y":755},{"directors":["韩寒"],"rate":"7.1","cover_x":6458,"star":"35","title":"后会无期","url":"https:\/\/movie.douban.com\/subject\/25805741\/","casts":["冯绍峰","陈柏霖","钟汉良","王珞丹","袁泉"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p2195469915.jpg","id":"25805741","cover_y":9213},{"directors":["大卫·弗兰科尔"],"rate":"7.9","cover_x":1693,"star":"40","title":"穿普拉达的女王","url":"https:\/\/movie.douban.com\/subject\/1482072\/","casts":["安妮·海瑟薇","梅丽尔·斯特里普","艾米莉·布朗特","斯坦利·图齐","西蒙·贝克"],"cover":"https://img3.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p735379215.jpg","id":"1482072","cover_y":2500},{"directors":["马丁·布莱斯"],"rate":"8.9","cover_x":518,"star":"45","title":"闻香识女人","url":"https:\/\/movie.douban.com\/subject\/1298624\/","casts":["阿尔·帕西诺","克里斯·奥唐纳","詹姆斯·瑞布霍恩","加布里埃尔·安瓦尔","菲利普·塞默·霍夫曼"],"cover":"https://img1.doubanio.com\/view\/movie_poster_cover\/lpst\/public\/p925123037.jpg","id":"1298624","cover_y":755}]}'
# datas=json.loads(js)
# # for data in datas['data']:
# #     a=data['directors'][0]
# #     for i in range(1,len(data['casts'])):
# #         a=a+','+data['directors'][i]
# #     print(a)
# if len(datas['data'])==20:
#         print('______')
# user_agent_list = [
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
#         "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#         "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
#         "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
#         "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
#         "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
#         "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
#         "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#         "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
#         "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
#         "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
#         "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
#        ]
#
# import random
# user_agent=random.choice(user_agent_list)
# print('\''+user_agent+'\'')
