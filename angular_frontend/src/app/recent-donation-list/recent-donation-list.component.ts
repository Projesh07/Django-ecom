import { Component, OnInit } from '@angular/core';
import {CampaignService} from '../campaign.service';
import {TopDonations} from '../campaign-model';

@Component({
  selector: 'recent-donation-list',
  templateUrl: './recent-donation-list.component.html',
  styleUrls: ['../top-donation-list/top-donation-list.component.css']
})
export class RecentDonationListComponent implements OnInit {

  recent_donations: TopDonations[];
  constructor(private campaignslist: CampaignService){
   }

  ngOnInit() {
    this.getRecentDonations();
  }

    getRecentDonations(): void {
    this.campaignslist.getRecentDonations()
          .subscribe(recent_donations => {
           this.recent_donations = recent_donations;
           console.log('data',recent_donations);
        });
	}

}