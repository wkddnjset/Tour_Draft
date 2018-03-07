import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, ViewController } from 'ionic-angular';

/**
 * Generated class for the PopoverPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-popover',
  templateUrl: 'popover.html',
})
export class PopoverPage {
  items:any;
  constructor(
  	public navCtrl: NavController, 
  	public navParams: NavParams,
  	public viewCtrl: ViewController,
  	) {
    this.items = this.navParams.get('listData');
    // console.log(this.items)
  }
  dismiss(item) {
    let data = item;
    this.viewCtrl.dismiss(data);
  }
  ionViewDidLoad() {
    // console.log('ionViewDidLoad PopoverPage');
  }
}
