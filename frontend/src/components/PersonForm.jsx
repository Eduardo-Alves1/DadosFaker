import React, { useState } from 'react';
import { Box, Button, TextField, Typography, Alert, CircularProgress, Chip, Stack } from '@mui/material';
import axios from 'axios';

export default function PersonForm() {
  const [fields, setFields] = useState(['nome', 'email', 'cpf']);
  const [fieldInput, setFieldInput] = useState('');
  const [quantity, setQuantity] = useState(1);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleAddField = () => {
    if (fieldInput && !fields.includes(fieldInput)) {
      setFields([...fields, fieldInput]);
      setFieldInput('');
    }
  };
  const handleDeleteField = (field) => {
    setFields(fields.filter(f => f !== field));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError(null);
    try {
      const res = await axios.post('/api/dadosfakes/generate/', {
        fields,
        quantity: Number(quantity),
      });
      setResult(res.data);
    } catch (err) {
      setError('Erro ao gerar dados de pessoas');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mb: 4, p: 2, border: '1px solid #eee', borderRadius: 2 }}>
      <Typography variant="h6" gutterBottom>Gerar Dados Customizados de Pessoas</Typography>
      <Stack direction="row" spacing={2} sx={{ mb: 2 }}>
        <TextField
          label="Campo"
          value={fieldInput}
          onChange={e => setFieldInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' ? (e.preventDefault(), handleAddField()) : null}
        />
        <Button variant="outlined" onClick={handleAddField}>Adicionar Campo</Button>
        <TextField
          label="Quantidade"
          type="number"
          value={quantity}
          onChange={e => setQuantity(e.target.value)}
          inputProps={{ min: 1, max: 100 }}
          required
        />
        <Button type="submit" variant="contained" disabled={loading}>
          {loading ? <CircularProgress size={24} /> : 'Gerar'}
        </Button>
      </Stack>
      <Box sx={{ mb: 2 }}>
        {fields.map(field => (
          <Chip key={field} label={field} onDelete={() => handleDeleteField(field)} sx={{ mr: 1, mb: 1 }} />
        ))}
      </Box>
      {result && (
        <Box sx={{ maxHeight: 300, overflow: 'auto', mt: 2 }}>
          <Alert severity="success">Dados gerados com sucesso!</Alert>
          <pre style={{ fontSize: 13 }}>{JSON.stringify(result, null, 2)}</pre>
        </Box>
      )}
      {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
    </Box>
  );
} 