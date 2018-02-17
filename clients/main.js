const path = require('path')
//const glob = require('glob')
const electron = require('electron')
//const autoUpdater = require('./auto-updater')

const BrowserWindow = electron.BrowserWindow
const app = electron.app

const debug = true

if (process.mas) app.setName('Electron APIs')

var mainWindow = null
var Menu = electron.Menu;
var ipc = require('electron').ipcMain;

var menuTemplate = [{
  label:'文件',
  submenu:[{
    label:'退出',
    click:function(){
      app.quit()
    }
  }]
},{
  label:'商品管理',
  submenu:[{
    label:'商品档案',
    click:function(){
      mainWindow.webContents.send('open-product-profile','new')
    }
  },{
    label:'商品分类',
    click:function(){
      mainWindow.webContents.send('open-product-category','new')
    }
  },{
    label:'供应商管理',
    click:function(){
      mainWindow.webContents.send('open-product-supplier','new')
    }
  },{
    label:'商品查询',
    click:function(){
      mainWindow.webContents.send('open-product-query','new')
    }
  }]
},{
  label:'销售管理',
  submenu:[{
    label:'销售概况',
    click:function(){
      mainWindow.webContents.send('open-retail-dashboard','new')
    }
  },{
    label:'销售单据',
    click:function(){
      mainWindow.webContents.send('open-retail-detail','new')
    }
  },{
    label:'日结记录',
    click:function(){
       mainWindow.webContents.send('open-retail-day-summary','new')
    }
  },{
    label:'销售查询',
    click:function(){
       mainWindow.webContents.send('open-retail-query','new')
    }
  }]
},{
  label:'库存管理',
  submenu:[{
    label:'库存概况',
    click:function(){
       mainWindow.webContents.send('open-repetory-dashboard','new')
    }
  },{
    label:'库存详情',
    click:function(){
       mainWindow.webContents.send('open-repetory-detail','new')
    }
  },{
    label:'库存查询',
    click:function(){
      mainWindow.webContents.send('open-repetory-query','new')
    }
  },{type:'separator'},{
    label:'库存盘点',
    click:function(){
      mainWindow.webContents.send('open-repetory-check','new')
    }
  },{
    label:'盘点记录',
    click:function(){
      mainWindow.webContents.send('open-repetory-check-record','new')
    }
  },{type:'separator'},{
    label:'店铺调货',
    click:function(){
      mainWindow.webContents.send('open-repetory-exchange','new')
    }
  },{
    label:'调货记录',
    click:function(){
      mainWindow.webContents.send('open-repetory-exchange-record','new')
    }
  }]
},{
  label:'员工管理',
  submenu:[{
    label:'部门管理',
    click:function(){
      mainWindow.webContents.send('open-department','new')
    }
  },{
    label:'角色管理',
    click:function(){
      mainWindow.webContents.send('open-role','new')
    }
  },{
    label:'员工档案',
    click:function(){
      mainWindow.webContents.send('open-employee-profile','new')
    }
  },{type:'separator'},{
    label:'权限管理',
    click:function(){
      mainWindow.webContents.send('open-authority','new')
    }
  },{
    label:'员工权限',
    click:function(){
      mainWindow.webContents.send('open-employee-authority','new')
    }
  }]
},{
  label:'店铺管理'
},{
  label:'数据报表'
},{
  label:'系统设置',
  submenu:[{
    label:'支付方式',
    click:function(){
      mainWindow.webContents.send('open-paytype','new')
    }
  }]
}];
var menu = Menu.buildFromTemplate(menuTemplate);
Menu.setApplicationMenu(menu);

function initialize () {
  var shouldQuit = makeSingleInstance()
  if (shouldQuit) return app.quit()

  // loadDemos()
  
  function createWindow () {
    var windowOptions = {
      width: 1080,
      minWidth: 680,
      height: 840,
      title: app.getName()
    }

    if (process.platform === 'linux') {
      windowOptions.icon = path.join(__dirname, '/assets/app-icon/png/512.png')
    }

    

    mainWindow = new BrowserWindow(windowOptions)
    mainWindow.loadURL(path.join('file://', __dirname, '/index.html'))

    // Launch fullscreen with DevTools open, usage: npm run debug
    if (debug) {
      mainWindow.webContents.openDevTools()
      mainWindow.maximize()
      //require('devtron').install()
    }

    mainWindow.on('closed', function () {
      mainWindow = null
    })
  }

  app.on('ready', function () {
    createWindow()
    //autoUpdater.initialize()
  })

  app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })

  app.on('activate', function () {
    if (mainWindow === null) {
      createWindow()
    }
  })
}

// Make this app a single instance app.
//
// The main window will be restored and focused instead of a second window
// opened when a person attempts to launch a second instance.
//
// Returns true if the current version of the app should quit instead of
// launching.
function makeSingleInstance () {
  if (process.mas) return false

  return app.makeSingleInstance(function () {
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore()
      mainWindow.focus()
    }
  })
}

// Require each JS file in the main-process dir
function loadDemos () {
  //var files = glob.sync(path.join(__dirname, 'main-process/**/*.js'))
  //files.forEach(function (file) {
  //  require(file)
  //})
  //autoUpdater.updateMenu()
}

// Handle Squirrel on Windows startup events
switch (process.argv[1]) {
  case '--squirrel-install':
    //autoUpdater.createShortcut(function () { app.quit() })
    break
  case '--squirrel-uninstall':
   // autoUpdater.removeShortcut(function () { app.quit() })
    break
  case '--squirrel-obsolete':
  case '--squirrel-updated':
    app.quit()
    break
  default:
    initialize()
}
