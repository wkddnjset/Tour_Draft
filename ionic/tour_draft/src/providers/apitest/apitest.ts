import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

/*
  Generated class for the ApitestProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ApitestProvider {
  api_id;
  url;

  constructor(public http: HttpClient) {
    console.log('Hello ApitestProvider Provider');
    this.url = 'http://localhost:8000/api/test/1/'
  }
  getApi(api_id){
  	return this.http.get(this.url+'?format=json')
  }
}
