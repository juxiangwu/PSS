# -*- coding -*-
# 用户信息测试

from config.appconfig import db
from model.user import User

# 添加数据
user1 = User(name = "Jan",address = "Guangzhou",phone = "13712346578",
            telephone = "+86-020-12345678",fax = "400010",qq = "123456789",
            email = "jan@iotservice.com",password = "adeesdfde")
# user1.id = -1
db.session.add(user1)
db.session.commit()
print(user1)

# 查询
#user = User.query.filter_by(id=1).all()
#print(user)
#users = User.query.order_by(User.name.desc()).limit(2).all()
#print(users)

# 更新
#user = User.query.filter_by(id=4).update({"name":"Jenson"})
#db.session.commit()
#print(user)

# 删除
# user = User.query.filter_by(id=1).first()
# db.session.delete(user)
# db.session.commit()
