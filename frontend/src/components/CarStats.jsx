import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper, CircularProgress, Alert, Grid } from '@mui/material';
import axios from 'axios';

export default function CarStats() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchStats = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await axios.get('/api/veiculos/veiculos/stats/');
      setStats(res.data.data || res.data);
    } catch (err) {
      setError('Erro ao buscar estatísticas');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStats();
  }, []);

  return (
    <Box sx={{ mb: 4 }}>
      <Typography variant="h6" gutterBottom>Estatísticas dos Veículos</Typography>
      {loading ? <CircularProgress /> : error ? <Alert severity="error">{error}</Alert> : stats && (
        <Paper sx={{ p: 2 }}>
          <Typography>Total de veículos: <b>{stats.total_veiculos}</b></Typography>
          <Grid container spacing={2} sx={{ mt: 1 }}>
            <Grid item xs={12} md={4}>
              <Typography variant="subtitle2">Por Categoria</Typography>
              <ul>
                {Object.entries(stats.por_categoria || {}).map(([cat, val]) => (
                  <li key={cat}>{cat}: <b>{val}</b></li>
                ))}
              </ul>
            </Grid>
            <Grid item xs={12} md={4}>
              <Typography variant="subtitle2">Por Marca</Typography>
              <ul>
                {Object.entries(stats.por_marca || {}).map(([marca, val]) => (
                  <li key={marca}>{marca}: <b>{val}</b></li>
                ))}
              </ul>
            </Grid>
            <Grid item xs={12} md={4}>
              <Typography variant="subtitle2">Por Situação</Typography>
              <ul>
                {Object.entries(stats.por_situacao || {}).map(([sit, val]) => (
                  <li key={sit}>{sit}: <b>{val}</b></li>
                ))}
              </ul>
            </Grid>
          </Grid>
        </Paper>
      )}
    </Box>
  );
} 