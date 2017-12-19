
import {Category} from './category';
import {Tag} from './tags-model';

import {CampaignComment} from './campaign-comment-model';
import {CampaignDonate} from './campaign-donate-model';
import {Document} from './document-model';

export interface Campaign{

id:Number;
title: string;
story:string;
amount:string;
start_date:string;
end_date:string;
status:Number;
publish_date:string;
category:Category;
documents:Document[];
campaign_donate:CampaignDonate[];
tags:Tag[];
total_donate:string;
campaign_comment:CampaignComment[];
}


export interface User{

id:Number;
amount: string;
first_name:string;
username:string;
email:string;
}


export interface TopDonations{

id:Number;
amount: string;
donate_at:string;
campaign:Campaign;
user:User;
}

export interface DonationComments{

id:Number;
comment: string;
comment_at:string;
created_at:string;
user:User;
campaign:Number;

}


