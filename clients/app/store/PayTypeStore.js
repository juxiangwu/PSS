Ext.define('PSS.store.PayTypeStore',{
	extend:'Ext.data.Store',
	model:'PSS.model.PayType',
	autoLoad: true,
	proxy:{
		type:'ajax',
		url:require('./config.json').host + '/query_paytype/'+require('./shop.json').shops[0].id,
		reader:{
			type:'json',
			root:'datas',
			totalProperty:'total'
		}
	}
});