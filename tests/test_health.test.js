const request = require('supertest');
const app = require('../src/app');

describe('GET /health/', () => {
  it('returns status ok and healthy message', async () => {
    const res = await request(app).get('/health/');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('ok');
    expect(res.body.message.toLowerCase()).toContain('healthy');
  });
});
