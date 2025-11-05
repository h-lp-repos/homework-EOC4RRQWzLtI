import { useState } from 'react'

export default function Home() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setAnswer('')
    try {
      const res = await fetch('http://localhost:8000/api/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ question })
      })
      const data = await res.json()
      setAnswer(data.answer)
    } catch (err) {
      console.error(err)
      setAnswer('Error obteniendo respuesta.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white rounded shadow p-6 w-full max-w-md">
        <h1 className="text-xl font-bold mb-4">CodeBase Q&A</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Escribe tu pregunta..."
            className="w-full p-2 border rounded"
            rows={3}
          />
          <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
            {loading ? 'Consultando...' : 'Preguntar'}
          </button>
        </form>
        {answer && (
          <div className="mt-6">
            <h2 className="font-semibold">Respuesta:</h2>
            <p className="mt-2 whitespace-pre-wrap">{answer}</p>
          </div>
        )}
      </div>
    </div>
  )
}
