Ext.define('PSS.product.PayTypeWin',{
	extend: 'Ext.ux.desktop.Module',
	requires:[
		'Ext.grid.Panel',
		'Ext.window.MessageBox',
		'PSS.model.PayType',
		'PSS.store.PayTypeStore',
		'PSS.controller.PayTypeController'
	],
	id:'paytype-win',
	init:function(){
		this.launcher = {
			text:'支付方式',
			iconCls:'product-16x16'
		}
	},
	createWindow:function(){
		var me = this;
		var desktop = me.app.getDesktop();
		var win = desktop.getWindow('paytype-win')
		if(win){
			return win;
		}
		me.gridpanelStore = Ext.create('PSS.store.PayTypeStore');
		me.controller = Ext.create('PSS.controller.PayTypeController');
		win = desktop.createWindow({
			id:'paytype-win',
			title:'支付方式',
			width:600,
			height:480,
			iconCls: 'product-16x16',
			animCollapse:false,
			border: false,
            layout: 'fit',
            items:[{
            	xtype:'gridpanel',
            	store:me.gridpanelStore,
            	columnLines: true,
            	columns:[
            		{text:'ID',dataIndex:'id'},
            		{text:'名称',dataIndex:'typeName'},
            		
            	],
            	listeners:{
            		itemclick:function( thiz, record, item, index, e, eOpts ){
            			me.selectedItem = record.data
            			console.log(me.selectedItem)
            		}
            	}
            }],
            tbar:{
            	xtype:'toolbar',
            	items:[{
            		xtype:'label',
            		text:'名称:'
            	},{
            		xtype:'textfield',
            		width:100,
            		id:'paytype-name-tf'
            	},{
            		xtype:'button',
            		text:'添加',
            		handler:function(){
            			var name = Ext.getCmp('paytype-name-tf').getValue();
            			if(!name){
            				Ext.msg.alert('添加支付方式','请输入支付方式');
            				return;
            			}
            			shopId = require('./shop.json').shops[0].id
            			console.log('shopId = ',shopId)
            			var datas = {
            				'shopId':shopId,
            				'typeName':name,
            				'typeValue':1
            			};
            			me.controller.add(datas,function(result){
            				if(result.success){
            					me.gridpanelStore.load();
            				}else{
            					Ext.Msg.alert('添加支付方式','错误:'+result.msg);
            				}
            			});
            			me.selectedItem = null;
            		}
            	},{
            		xtype:'button',
            		text:'更新',
            		handler:function(){
            			var name = Ext.getCmp('paytype-name-tf').getValue();
            			if(!name){
            				Ext.msg.alert('更新支付方式','请输入支付方式');
            				return;
            			}
            			if(!me.selectedItem){
            				Ext.Msg.alert('更新支付方式','请选择要更新的支付方式');
            				return;
            			}
            			var datas = {
            				'id':me.selectedItem.id,
            				'shopId':me.selectedItem.shopId,
            				'typeValue':me.selectedItem.typeValue,
            				'typeName':name
            			};
            			me.controller.update(datas,function(result){
            				if(result.success){
            					me.gridpanelStore.load();
            				}else{
            					Ext.Msg.alert('更新支付方式','错误:'+result.msg);
            				}
            			})
            		}
            	},{
            		xtype:'button',
            		text:'删除',
            		handler:function(){
            			if(!me.selectedItem){
            				Ext.Msg.alert('删除支付方式','请选择要删除的支付方式');
            				return;
            			}
            			var datas = {
            				'id':me.selectedItem.id,
            				'shopId':me.selectedItem.shopId
            			};
            			me.controller.remove(datas,function(result){
            				if(result.success){
            					me.gridpanelStore.load();
            				}else{
            					Ext.Msg.alert('删除支付方式','错误:'+result.msg);
            				}
            			});
            		}
            	},{
            		xtype:'button',
            		text:'刷新',
            		handler:function(){
            			me.gridpanelStore.load();
            		}
            	}]
            }
		})

		return win;
	}


});