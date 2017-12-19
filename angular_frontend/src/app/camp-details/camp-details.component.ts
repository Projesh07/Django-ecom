import { Component, OnInit } from '@angular/core';
import {CampaignService} from '../campaign.service';
import {Campaign,DonationComments} from '../campaign-model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'camp-details',
  templateUrl: './camp-details.component.html',
  styleUrls: ['./camp-details.component.css']
})
export class CampDetailsComponent implements OnInit {

  campaign:Campaign;
  comments:DonationComments[];
  private  param;
  private id;

  constructor(private campaignslist: CampaignService,private activatedRoute: ActivatedRoute) {
  		let params: any = this.activatedRoute.snapshot.params;
  		
  		this.param=params.slug;
  		
  
  		
   }  
   ngOnInit() {
    this.getCampaignDetails(this.param);

  }  
  getCampaignDetails(id): void {
    this.campaignslist.getCampaignDetails(id)
        .subscribe(campaign=> {
          this.campaign = campaign;
          console.log(this.campaign);
          this.id = this.campaign.id;
        });
  }


  getDonationComments(id): void {
    this.campaignslist.getDonationComments(id)
        .subscribe(comments=> {
          this.comments = comments;
          console.log(this.comments);
        });
  }
 
}
