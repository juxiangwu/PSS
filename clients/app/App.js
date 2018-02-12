/*!
 * Ext JS Library
 * Copyright(c) 2006-2014 Sencha Inc.
 * licensing@sencha.com
 * http://www.sencha.com/license
 */

Ext.define('PSS.App', {
    extend: 'Ext.ux.desktop.App',

    requires: [
        'Ext.window.MessageBox',
        'Ext.form.field.HtmlEditor',
        'Ext.ux.desktop.ShortcutModel',
        'Ext.chart.*',
        'PSS.components.MainProcessMessager',
        'PSS.Settings',
        'PSS.components.LevelDB',
        'PSS.view.product.ProductCategoryWin',
        'PSS.view.department.DepartmentWin'
    ],
    host:'http://192.168.0.1.4:3000',
    init: function() {
        // custom logic before getXYZ methods get called...
        var me = this;
        me.leveldb = new PSS.components.LevelDB();
        me.leveldb.initdb();
        
        this.callParent();
        this.mainProcessMessager = new PSS.components.MainProcessMessager(me)
        console.log(me);
        // now ready...
    },

    getModules : function(){
        return [
            new PSS.view.product.ProductCategoryWin()
            new PSS.view.department.DepartmentWin()
           // new Desktop.VideoWindow(),
            //new Desktop.Blockalanche(),
            // new PSS.SystemStatus(),
           // new Desktop.GridWindow(),
           // new Desktop.TabWindow(),
           // new Desktop.AccordionWindow(),
           // new Desktop.Notepad(),
            // new PSS.BogusMenuModule(),
            // new PSS.BogusModule()
        ];
    },

    getDesktopConfig: function () {
        var me = this, ret = me.callParent();

        return Ext.apply(ret, {
            //cls: 'ux-desktop-black',

            contextMenuItems: [
                { text: 'Change Settings', handler: me.onSettings, scope: me }
            ],

            shortcuts: Ext.create('Ext.data.Store', {
                model: 'Ext.ux.desktop.ShortcutModel',
                data: [
                    { name: '商品分类', iconCls: 'product-32x32', module: 'product-category-win' },
                   
                ]
            }),

            wallpaper: 'resources/images/wallpapers/Blue-Sencha.jpg',
            wallpaperStretch: true
        });
    },

    // config for the start menu
    getStartConfig : function() {
        var me = this, ret = me.callParent();

        return Ext.apply(ret, {
            title: 'Don Griffin',
            iconCls: 'user',
            height: 300,
            toolConfig: {
                width: 100,
                items: [
                    {
                        text:'Settings',
                        iconCls:'settings',
                        handler: me.onSettings,
                        scope: me
                    },
                    '-',
                    {
                        text:'Logout',
                        iconCls:'logout',
                        handler: me.onLogout,
                        scope: me
                    }
                ]
            }
        });
    },

    getTaskbarConfig: function () {
        var ret = this.callParent();

        return Ext.apply(ret, {
            quickStart: [
               // { name: 'Accordion Window', iconCls: 'accordion', module: 'acc-win' },
               // { name: 'Grid Window', iconCls: 'icon-grid', module: 'grid-win' }
            ],
            trayItems: [
                { xtype: 'trayclock', flex: 1 }
            ]
        });
    },

    onLogout: function () {
        Ext.Msg.confirm('Logout', 'Are you sure you want to logout?');
    },

    onSettings: function () {
        var dlg = new PSS.Settings({
            desktop: this.desktop
        });
        dlg.show();
    }
});
