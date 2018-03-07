import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

/**
 * Generated class for the ItemtwoPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-itemtwo',
  templateUrl: 'itemtwo.html',
  
})
export class ItemtwoPage {

  constructor(
  	public navCtrl: NavController, 
  	public navParams: NavParams
  	) {
  }
  ionViewDidLoad() {
    console.log('ionViewDidLoad ItemtwoPage');
  }

}
