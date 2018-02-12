Ext.define('PSS.view.product.ProductCategoryWin',{
	extend: 'Ext.ux.desktop.Module',
	requires:[
		'PSS.store.ProductCategoryStore',
		'PSS.controller.ProductCategoryController',
		'Ext.tree.Panel',
		'Ext.panel.Panel',
		'Ext.toolbar.Toolbar'
	],
	id:'product-category-win',

	init:function(){
		this.launcher = {
			text:'商品分类',
			iconCls:'product-16x16'
		}
	},

	createWindow:function(){
		var me = this;
		me.productCategoryController = Ext.create('PSS.controller.ProductCategoryController');
		var desktop = this.app.getDesktop()
		var win = desktop.getWindow('product-category-win');
		me.selectedCategoryItem = null;
		if(win){
			return win;
		}
		var treeStore = Ext.create('PSS.store.ProductCategoryStore')
		treeStore.setContext(this.app)
		win = desktop.createWindow({
			id:'product-category-win',
			title:'商品分类',
			width:600,
			height:400,
			iconCls: 'product-16x16',
			animCollapse:false,
            border: false,
            layout: 'fit',
            items:[{
            	xtype:'treepanel',
            	width:'100%',
            	height:'100%',
            	id:'category-tree-panel',
            	rootVisible: true,
            	store:treeStore,
            	listeners:{
            		itemclick:function( thiz, record, item, index, e, eOpts ) {
            			me.selectedCategoryItem = record.data;
            			console.log(me.selectedCategoryItem);
            		}
            	}
            }],
            tbar:{
            	xtype:'toolbar',
            	items:[
            		{
            			xtype:'label',
            			text:'分类名称:'
            		},
            		{
            			xtype:'textfield',
            			id:'product-category-name-tf',
            			width:100
            		},
            		{
            			xtype:'button',
            			text:'添加',
            			handler:function(){
            				var name = Ext.getCmp('product-category-name-tf').getValue()
            				if(!name){
            					Ext.Msg.alert('添加商品分类','请输入分类名称')
            					return
            				}
            				
            				var treepanel = Ext.getCmp('category-tree-panel');
            				// var selectNode = treepanel.getSelection();
            				// console.log(selectNode)
            				var datas = {}
            				if(me.selectedCategoryItem){
            					datas.name = name;
            					datas.shopId = 1;//selectNode.shopId;
            					datas.pid = me.selectedCategoryItem.id;

            				}else{
            					datas.name = name;
            					datas.shopId = 1;
            					datas.pid = -1;
            				}
            				//console.log(selectNode.pid,selectNode.name,selectNode.id)
            				// console.log(datas)
            				
            				me.productCategoryController.add(datas,function(result){
            					if(result.success){
            						treepanel.store.load();
            					}else{
            						Ext.Msg.alert('添加商品分类','错误:'+result.msg);
            					}
            				})
            			}//handler
            		},{//button:添加
            			xtype:'button',
            			text:'删除',
            			handler:function(){
            				var treepanel = Ext.getCmp('category-tree-panel');
            				if(!me.selectedCategoryItem){
            					Ext.Msg.alert('删除商品分类','请选择一个分类');
            					return
            				}
            				var datas = {
            					// id:me.selectedCategoryItem.id,
            					// shopId:me.selectedCategoryItem.shopId
            				};
            				if(me.selectedCategoryItem.id == -1){
            					datas.id = me.selectedCategoryItem.id,
            					datas.shopId = 1
            				}else{
            					datas.id = me.selectedCategoryItem.id,
            					datas.shopId = me.selectedCategoryItem.shopId
            				}

            				me.productCategoryController.remove(datas,function(result){
            					if(result.success){
            						treepanel.store.load()
            					}else{
            						Ext.Msg.alert('删除商品分类','错误:'+result.msg)
            					}
            				})
            			}
            		},{
            			xtype:'button',
            			text:'更新',
            			handler:function(){
            				var treepanel = Ext.getCmp('category-tree-panel');
            				if(!me.selectedCategoryItem){
            					Ext.Msg.alert('更新商品分类','请选择一个分类');
            					return;
            				}
            				if(me.selectedCategoryItem.id == -1){
            					Ext.Msg.alert('更新商品分类','根分类不用更新');
            					return;
            				}

            				var name = Ext.getCmp('product-category-name-tf').getValue()
            				if(!name){
            					Ext.Msg.alert('添加商品分类','请输入分类名称')
            					return
            				}
            				var datas = {
            					shopId:me.selectedCategoryItem.shopId,
            					name:name,
            					id:me.selectedCategoryItem.id
            				};
            				me.productCategoryController.update(datas,function(result){
            					if(result.success){
            						treepanel.store.load();
            					}else{
            						Ext.Msg.alert('更新商品分类','错误:'+result.msg);
            					}
            				})
            			}
            		},{
            			xtype:'button',
            			text:'刷新',
            			handler:function(){
            				var treepanel = Ext.getCmp('category-tree-panel');
            				treepanel.store.load()
            			}
            		}

            	]
            }
		});

		return win;
	}
});