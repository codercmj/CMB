# encoding=gbk
import jieba
import csv
file_object2=open(r'C:\Users\86182\Desktop\zsyh\\test_data.csv').read().split('\n')  #һ���еĶ�ȡ����
Rs2=[] #�����洢�ִʵ��б�
for i in range(len(file_object2)):
    result=[]
    seg_list = jieba.cut(file_object2[i])
    for w in seg_list :#��ȡÿһ�зִ�
        result.append(w)
    Rs2.append(result)#�����зִ�д���б���ʽ���ִܷ��б�
    #д��CSV
file=open(r'C:\Users\86182\Desktop\\test_data_new.csv','w')
writer = csv.writer(file)#����д���ʽ
writer.writerows(Rs2)#����д��
    #file.write(str(Rs))
file.close()