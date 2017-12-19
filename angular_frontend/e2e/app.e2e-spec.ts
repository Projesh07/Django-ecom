import { DonationAnglularPage } from './app.po';

describe('donation-anglular App', () => {
  let page: DonationAnglularPage;

  beforeEach(() => {
    page = new DonationAnglularPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
