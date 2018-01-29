import { Component } from '@angular/core';

import { AboutPage } from '../about/about';
import { ContactPage } from '../contact/contact';
import { HomePage } from '../home/home';

import { NavParams } from 'ionic-angular';

@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {

  tab1Root = HomePage;
  tab2Root = AboutPage;
  tab3Root = ContactPage;

  // homeParam = {token : this.navPar.get('token')}

  constructor(private navPar: NavParams) {
  	this.homeParam = {token : this.navPar.get('token')}
  }
}
