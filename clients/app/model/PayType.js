Ext.define('PSS.model.PayType',{
	extend:'Ext.data.Model',
	fields:[
		{'name':'id','type':'int'},
		{'name':'typeName','type':'string'},
		{'name':'typeValue','type':'int'},
		{'name':'shopId','type':'int'}
	]
});