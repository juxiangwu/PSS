Ext.define('PSS.view.department.DepartmentWin',{
	extend: 'Ext.ux.desktop.Module',
	requires:[
		'PSS.store.DepartmentTreeStore',
		'PSS.controller.ProductCategoryController',
		'Ext.tree.Panel',
		'Ext.panel.Panel',
		'Ext.toolbar.Toolbar'
	],	
	id:'department-win',
	init:function(){
		//TODO:添加Start菜单
	},

	createWindow:function(){
		var me = this;
		me.departmentController = Ext.create('PSS.controller.ProductCategoryController');
		var desktop = me.getDesktop();
		var win = desktop.getWindow('department-win');
		if(win){
			return win;
		}
		var treeStore = Ext.createWindow('PSS.store.DepartmentTreeStore');
		win = desktop.createWindow({
			id:'department-win',
			title:'部门管理',
			width:600,
			height:800,
			iconCls:'product-16x16',
			animCollapse:false,
			border:false,
			layout:'fit',
			items:[{
				xtype:'treepanel',
				width:'100%',
				height:'100%',
				id:'department-manager-treepanel',
				rootVisible:true,
				store:treeStore,
				listeners:{
					itemclick:function(thiz,record,item,index,e,eOpts){
						me.selectedDepartmentItem = record.data
					}
				}
			}],
			tbar:{
				xtype:'toolbar',
				items:[{
					xtype:'label'
					text:'部门名称:'

				},{
					xtype:'textfield',
					id:'department-manager-name-tf',
					width:100
				},{
					xtype:'button',
					text:'添加',
					handler:function(){
						var name = Ext.getCmp('department-manager-name-tf').getValue();
						if(!name){
							Ext.Msg.alert('添加部门','请先输入部门名称');
							return;
						}
						var treepanel = Ext.getCmp('department-manager-treepanel');
						var datas = {};
						if(me.selectedDepartmentItem){
							datas.name = name;
							datas.shopId = 1;
							datas.pid = me.selectedDepartmentItem.id
						}else{
							datas.name = name;
							datas.shopId = 1;
							datas.pid = -1
						}

						me.departmentController.add(datas,function(result){
							if(result.success){
								treepanel.store.load();
							}else{
								Ext.Msg.alert('添加部门','错误:'+result.msg);
							}
						});
					}
				},{
					xtype:'button',
					text:'删除',
					handler:function(){
						var treepanel = Ext.getCmp('department-manager-treepanel');
						if(!me.selectedDepartmentItem){
							Ext.Msg.alert('删除部门','请选择一个分类');
							return;
						}

						var datas = {};
						if(me.selectedDepartmentItem.id == -1){
							datas.id = me.selectedDepartmentItem.id
							datas.shopId = 1
						}else{
							datas.id = me.selectedDepartmentItem.id
							datas.shopId = me.selectedDepartmentItem.shopId
						}

						me.departmentController.remove(datas,function(result){
							if(result.success){
								treepanel.store.load();
							}else{
								Ext.Msg.alert('删除部门','错误:'+result.msg);
							}
						});
					}	
				},{
					xtype:'button',
					text:'更新',
					handler:function(){
						var treepanel = Ext.getCmp('department-manager-treepanel');
						if(!me.selectedDepartmentItem){
							Ext.Msg.alert('更新部门','请选择一个部门');
							return;
						}
						if(me.selectedDepartmentItem.id == -1){
							Ext.Msg.alert('更新部门','根节点不用更新');
							return;
						}
						var name = Ext.getCmp('department-manager-name-tf').getValue()
						if(!name){
							Ext.Msg.alert('更新部门','请输入新的部门名称');
							return;
						}

						var datas = {
							shopId:me.selectedDepartmentItem.shopId,
							name:name,
							id:me.selectedDepartmentItem.id
						};

						me.departmentController.update(datas,function(result){
							if(result.success){
								treepanel.store.load();
							}else{
								Ext.Msg.alert('更新部门','错误:'+result.msg);
							}
						});
					}
				},{
					xtype:'button',
					text:'刷新',
					handler:function(){
						Ext.getCmp('department-manager-treepanel').store.load()
					}
				}]
			}
		});

		return win;
	}
})