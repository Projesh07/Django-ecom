import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaignBoxComponentComponent } from './campaign-box-component.component';

describe('CampaignBoxComponentComponent', () => {
  let component: CampaignBoxComponentComponent;
  let fixture: ComponentFixture<CampaignBoxComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaignBoxComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaignBoxComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
