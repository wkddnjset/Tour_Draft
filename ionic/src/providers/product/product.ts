import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable()
export class ProductProvider {
  server_url = "http://127.0.0.1:8000/api";
  json_format = "/?format=json";

  constructor(public http: HttpClient) {
    console.log('RESTful API Server Product Service');
  }


  getItemList(){
  	return this.http.get(this.server_url + '/items' + this.json_format)
  }
}
