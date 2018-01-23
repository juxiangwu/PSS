drop if exists databae pss;
create databae pss;
use pss;
# 创建用户信息表
drop table if exists t_user;
create table t_user(id int not null primary key auto_increment,name varchar(128),
		address varchar(1024),phone varchar(16),telephone varchar(32),fax varchar(32),
		qq varchar(32),email varchar(128),password varchar(1024));
# 创建商店信息表
# name:商店名称
# address:商店地址
# owner_id:用户ID
drop table if exists t_shop ;
create table t_shop(id int not null primary key auto_increment,name varchar(128),
		address varchar(1024),owner_id int);

# 创建供应商信息表
drop table if exists t_supplier_info;
create table t_supplier_info(id int not null primary key auto_increment,name varchar(128),
		address varchar(1024),phone varchar(16),telephone varchar(32),fax varchar(32),
		qq varchar(32),email varchar(128),shop_id int,owner_id int);
        
# 创建商品分类表
# name:分类名称
# shop_id:商店ID
# category_parent_id:上级分类ID
drop table if exists t_product_category;
create table t_product_category(id int not null primary key auto_increment,name varchar(128),
			shop_id int,category_parent_id int,lft int,rgt int);
            
# 创建商品基础信息表
# shop_id:所属商店
# name:商品名称
# code:商品编码
# barcode:商品条码
# pinyin_code:拼音码
# category_id:分类ID
# category_name:分类名称
# unit_name:单位名称
# puchase_price:进货价
# sell_price:零售价
# wholesale_price:批发价
# supplier_name:供应商
# supplier_id:供应商ID
# is_enabled:是否启用
drop table if exists t_product_base_info;
create table t_product_base_info(id int not null primary key auto_increment,
		shop_id int,
		name varchar(128),
		code varchar(128),
		barcode varchar(128),
		pinyin_code varchar(128),
		category_name varchar(128),
		category_id int,
		unit_name varchar(128),
		puchase_price float,
		sell_price float,
		wholesale_price float,
		supplier_name varchar(128),
		supplier_id int,
		create_datetime datetime,
		modify_datetime datetime,
		is_enabled bool);
        
# 创建商品SKU信息表
# shop_id:商店ID
# product_id:商品ID
# sku_code:SKU编码
# store_counts:SKU库存数量
drop table if exists t_product_sku_info;
create table t_product_sku_info(id int not null primary key auto_increment,
		shop_id int,
		product_id int,
		sku_code varchar(128),
		store_counts int);
        
# 创建商品SKU属性信息表
# shop_id:商店ID
# product_id:商品ID
# sku_id: SKU ID
# product_prop_id:商品属性ID
drop table if exists t_product_sku_property;
create table t_product_sku_property(id int not null primary key auto_increment,
		shop_id int,
		product_id int,
		sku_id int,
		product_prop_id int);
        
# 创建商品属性信息表
# shop_id:商店ID
# product_id:商品ID
# prop_type:属性类型
# prop_name:属性名称
# prop_value:属性类型，1:SKU属性,2:整数型,3:浮点型,4:字符串型,5:日期型
drop table if exists t_product_property;
create table t_product_property(id int not null primary key auto_increment,
		shop_id int,
		product_id int,
		prop_type int,
		prop_name varchar(128),
		prop_value varchar(1024));
        
# 创建商品库存信息表
# shop_id:商店ID
# product_id:商品ID
# sku_id:SKU ID
# 当不使用SKU时，sku_id的值默认为0,total_counts表示商品所有库存量
# 当使用SKU时，total_counts表示单个商品的库存量
drop table if exists t_product_repertory;
create table t_product_repertory(id int not null primary key auto_increment,
		shop_id int,product_id int,sku_id int,total_counts int);
        
        
# 创建商品库存变动信息表
# shop_id:商店ID
# product_id:商品ID
# sku_id:SKU ID
# changed_date:变动日期
# changed_type:变动类型,-1未定义,1销售,2进货,3退货,4调入,5调出
# operator_id:操作员
drop table if exists t_product_repertory_changed;
create table t_product_repertory_changed(id int not null primary key auto_increment,
		shop_id int,product_id int,sku_id int,changed_count int,changed_date date,changed_type int,
		operator_id int);
        
# 创建部门
drop table if exists t_department_info;
create table t_department_info(id int not null primary key auto_increment,
		shop_id int,name varchar(128),parent_id int,lft int,rgt int);
        
# 创建角色
drop table if exists t_employee_role;
create table t_employee_role(id int not null primary key auto_increment,
		shop_id int,name varchar(128));
        
# 创建员工信息表
drop table if exists t_employee_info;
create table t_employee_info(id int not null primary key auto_increment,
		shop_id int,name varchar(128),password varchar(1024),telephone varchar(16),
		email varchar(512),department_id int,role_id int);

# 创建员工权限表
drop table if exists t_employee_authority;
create table t_employee_authority(id int not null primary key auto_increment,
		shop_id int,employee_id int,authority_id int);
        
# 创建角色权限
drop table if exists t_role_authority;
create table t_role_authority(id int not null primary key auto_increment,
		shop_id int,name varchar(128),role_value int);
        
# 创建零售信息表
# order_id:订单流水号
# shop_id:商店ID
# operator_id:操作员ID
# retail_type:1销售,2退货,3换货
# retail_date:订单发生时间
# order_total_price:订单总金额
# order_counts:订单商品总数
# member_id:会员ID
# order_real_price:订单实收金额
# order_profit:订单利润
# order_desc:订单描述
drop table if exists t_retail_detail;
create table t_retail_detail(id int not null primary key auto_increment,
		order_id varchar(128),shop_id int,operator_id int,retail_type int,
		retail_date datetime,order_total_price float,product_counts int,member_id int,
		order_real_price float,order_profit float,order_desc varchar(1024));
        
# 创建零售详情表
# shop_id:商店ID
# order_id:订单ID
# product_id:商品ID
# sku_id:SKU ID
# product_discount:商品折扣
# product_directly_sub:商品直减
drop table if exists t_retail_item_detail;
create table t_retail_item_detail(id int not null primary key auto_increment,
		shop_id int,order_id int,product_id int,sku_id int,product_discount float,product_directly_sub float);