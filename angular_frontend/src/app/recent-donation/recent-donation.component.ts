import { Component, OnInit,Input } from '@angular/core';
import * as moment from 'moment'

@Component({
  selector: 'recent-donation',
  templateUrl: './recent-donation.component.html',
  styleUrls: ['../top-donation/top-donation.component.css']
})
export class RecentDonationComponent implements OnInit {

@Input() donar_name;
@Input() donate_time;
@Input() donate_amount;

  constructor() { }

  ngOnInit() {
  }

}
