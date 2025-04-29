describe('Login Page', () => {
  it('should allow a user to login', () => {
    // 1. Visit the login page
    cy.visit('/login');

    // 2. Fill in username and password
    cy.get('[data-cy="username"]').type('manos');
    cy.get('[data-cy="password"]').type('manos123');

    // 3. Click login button
    cy.get('[data-cy="login-button"]').click();

    // 4. Verify login success
    // Example: maybe it redirects to a dashboard
    cy.url().should('include', '/dashboard');

    
  });
});
