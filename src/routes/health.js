const express = require('express');
const router = express.Router();

/**
 * Simple health check endpoint
 */
router.get('/', (req, res) => {
  res.json({ status: 'ok', message: 'Service is healthy' });
});

module.exports = router;
