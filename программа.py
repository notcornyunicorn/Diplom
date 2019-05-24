def main():

    f = open(r'C:\Users\miair\Desktop\ДИПЛОМ\данные\база.txt', 'r', encoding = 'utf-8')
    a = f.readlines()
    f.close() #читает базу данных
    
    a1, a2, a3 = [], [], []
    adj, hard, soft, ow, ec, iny, yn, aw, n, yjn, aln, arn, czn, enn, ist, liw, teln, owat, at, sk, ck, ni, k = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
    d = {}
    
    for line in a:
        line = line.split('\t')
        del line[2]
        del line[4]
        del line[2]
        a1.append(line) #превращает базу в массив строк, состоящих из массива 'число', 'слово', 'число' 

    d = {a1[i][0]:a1[i][1] for i in range(len(a1))} #создает словарь производящих слов
    
    for line in a1:
        if line[2] == '':
            a2.append([line[1], ''])
        else:
            try:
                a2.append([line[1], d[line[2]]])
            except KeyError:
                continue #создает массив 'производное слово', 'производящее слово'

    for line in a2:
        if line[0][0].islower(): #убирает слова, начинающиеся с большой буквы
            if line[1] == '':
                a3.append(line)
            else:
                if line[0][:3] == line[1][:3].lower():
                    a3.append(line) #убирает слова, образованные с помощью приставок
                
    for line in a3:
        word = line[0] + '\t' + line[1] + '\n'
        if line[0][-1] == 'y':
            adj += word
            hard += word
            if line[0][-3:-1] == 'ow':
                ow += word
            if line[0][-3:-1] == 'ęc':
                ec += word
            if line[0][-3:-1] == 'in':
                iny += word
            if line[0][-3:-1] == 'yn':
                yn += word
            if line[0][-3:-1] == 'aw':
                aw += word
            if line[0][-2:-1] == 'n':
                n += word
            if line[0][-4:-1] == 'yjn':
                yjn += word
            if line[0][-4:-1] == 'aln':
                aln += word
            if line[0][-4:-1] == 'arn':
                arn += word
            if line[0][-4:-1] == 'czn':
                czn += word
            if line[0][-4:-1] == 'enn':
                enn += word
            if line[0][-4:-1] == 'ist':
                ist += word
            if line[0][-4:-1] == 'liw':
                liw += word
            if line[0][-5:-1] == 'teln':
                teln += word
            if line[0][-5:-1] == 'owat':
                owat += word
            if line[0].endswith('aty') and line[0][-5:] != 'owaty':
                at += word            
        if line[0][-1] == 'i':
            adj += word
            soft += word
            if line[0][-3:-1] == 'sk':
                sk += word
            if line[0][-3:-1] == 'ck':
                ck += word
            if line[0][-2:-1] == 'n':
                ni += word
            if line[0].endswith('ki'):
                if line[0][-3:] != 'ski' and line[0][-3:] != 'cki':
                    k += word #записывает в переменную слова с одним и тем же суффиксом
                    
        
    files = [r'C:\Users\miair\Desktop\ДИПЛОМ\данные\прилагательные.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\твердая финаль.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\мягкая финаль.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\ow.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\ec.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\in.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\yn.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\aw.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\n.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\yjn.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\aln.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\arn.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\czn.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\enn.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\ist.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\liw.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\teln.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\owat.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\at.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\sk.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\ck.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\ni.txt', r'C:\Users\miair\Desktop\ДИПЛОМ\данные\k.txt']
    values = [adj, hard, soft, ow, ec, iny, yn, aw, n, yjn, aln, arn, czn, enn, ist, liw, teln,
              owat, at, sk, ck, ni, k]
    for index, file in enumerate(files):
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(values[index]) #записывает переменные в файлы
    
   
if __name__=='__main__':
    main()
