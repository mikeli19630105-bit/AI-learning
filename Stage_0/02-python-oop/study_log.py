# 学习记录管理器：用类来组织数据和行为

class StudyLog:
    # 初始化：创建对象时自动运行
    ##？ 一个类中__init__只能写一次吗？
    def __init__(self, filename='study_log.txt'):
        self.filename = filename  #存文件名
        self.records = []         #存所有记录的空列表

    #添加一条记录
    ##  这里是写一个函数，来录入日期，内容，学习时间
    def add_record(self, date, content, hours):
        self.records.append({"date": date, "content" :content, "hours":hours})

    # 保存到文件（CSV 格式）
    ##？ 为什么要保存成CSV格式  和 TXT格式的区别是什么
    def save(self):
            with open(self.filename, 'w', encoding='utf-8') as f:
                 for r in self.records:
                    f.write(f"{r['date']},{r['content']},{r['hours']}\n")

# ===== 测试 =====
log = StudyLog()##? 这句是什么意思
log.add_record('2026-09-13', 'study OOP', 2.0)
log.add_record('2026-09-14', 'study NumPy', 1.5)
log.save()

print('已保存到 study_log.txt')