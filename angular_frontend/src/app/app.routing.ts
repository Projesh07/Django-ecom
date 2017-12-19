import {ModuleWithProviders} from "@angular/core";
import {Routes, RouterModule} from "@angular/router";

import { HomeComponentComponent } from './home-component/home-component.component';
import { CampaignComponentComponent } from './campaign-component/campaign-component.component';
import { CampaingnPageComponent } from './campaingn-page/campaingn-page.component';


const appRoutes : Routes = [
    {   
        path:'',
        component: HomeComponentComponent,
        pathMatch: 'full'
    },
    {
        path:'categories/:id',
        component: CampaignComponentComponent,
        pathMatch: 'full'
    },
    {
        path:'campdetails/:slug',
        component: CampaingnPageComponent,
        pathMatch: 'full'
    }
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
