import React, { useState } from 'react';
import { Box, Button, Typography, Alert, CircularProgress } from '@mui/material';
import axios from 'axios';

export default function PersonProfile() {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGetProfile = async () => {
    setLoading(true); setError(null); setProfile(null);
    try {
      const res = await axios.get('/api/dadosfakes/dados-prontos/');
      setProfile(res.data[0]);
    } catch (err) {
      setError('Erro ao buscar perfil pronto');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ mb: 4, p: 2, border: '1px solid #eee', borderRadius: 2 }}>
      <Typography variant="h6" gutterBottom>Perfil Pronto de Pessoa</Typography>
      <Button variant="contained" onClick={handleGetProfile} disabled={loading} sx={{ mb: 2 }}>
        {loading ? <CircularProgress size={24} /> : 'Gerar Perfil Pronto'}
      </Button>
      {profile && (
        <Box sx={{ maxHeight: 300, overflow: 'auto', mt: 2 }}>
          <Alert severity="info">
            <pre style={{ fontSize: 13 }}>{JSON.stringify(profile, null, 2)}</pre>
          </Alert>
        </Box>
      )}
      {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
    </Box>
  );
} 