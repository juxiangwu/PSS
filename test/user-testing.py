# -*- coding -*-
# 用户信息测试

from config.appconfig import db
from model.user import User

# 添加数据
#user1 = User("Jan","Guangzhou","13712346578","+86-020-12345678","400010","123456789","jan@iotservice.com","adeesdfde")

#db.session.add(user1)
#db.session.commit()
#print(user1)

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
#user = User.query.filter_by(id=3).first()
#db.session.delete(user)
#db.session.commit()
