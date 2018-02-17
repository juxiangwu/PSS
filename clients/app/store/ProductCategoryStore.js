Ext.define('PSS.store.ProductCategoryStore',{
	extend:'Ext.data.TreeStore',
	requires:[
		'Ext.data.TreeStore'
		//'Ext.util.Cookies'
	],
	context:null,
	setContext:function(ctx){
		this.context = ctx;
	},
	//alias:'store.productcategory',
	xtype:'productcategorystore',
	fields:[
		{name:'id'},{name:'pid'},{name:'text'},{name:'name'},{name:'leaf'},{name:'shopId'}
	],
	shopId:Ext.util.Cookies.get('shopId'),
	userId:Ext.util.Cookies.get('userId'),
	proxy:{
		type:'ajax',
		url:require('./config.json').host + '/query_category/'+ require('./config.json').userId + '/' +  + require('./shop.json').shops[0].id,
		reader:{
			type:'json',
			root:'datas',
			totalProperty:'total'
		},
	},
	
	root:{
		text:'分类',
		id:-1,
		expanded: true
	}
});