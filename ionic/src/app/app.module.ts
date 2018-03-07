import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { HttpClientModule } from '@angular/common/http';

import { MyApp } from './app.component';
import { HomePage } from '../pages/home/home';
import { ListPage } from '../pages/list/list';
import { ItemonePage } from '../pages/itemone/itemone';
import { ItemtwoPage } from '../pages/itemtwo/itemtwo';
import { ItemthreePage } from '../pages/itemthree/itemthree';
import { PopoverPage } from '../pages/popover/popover';

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AnimationService, AnimatesDirective } from 'css-animator';
import { ProductProvider } from '../providers/product/product';

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    ListPage,
    ItemonePage,
    ItemtwoPage,
    ItemthreePage,
    PopoverPage,
    AnimatesDirective
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    IonicModule.forRoot(MyApp),
    BrowserAnimationsModule,
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    ListPage,
    ItemonePage,
    ItemtwoPage,
    ItemthreePage,
    PopoverPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    AnimationService,
    ProductProvider
  ]
})
export class AppModule {}
