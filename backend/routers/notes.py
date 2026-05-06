from fastapi import APIRouter, HTTPException
from datetime import datetime
from backend.schemas.note import NoteItem
from backend.services.firebase import db

router = APIRouter()

@router.post("/notes")
def create_note(note: NoteItem):
    try:
        doc_ref = db.collection("notes").document()
        new_note = {
            "user_email": note.user_email,
            "content": note.content,
            "created_at": datetime.now().isoformat()
        }
        doc_ref.set(new_note)
        return {"status": "success", "message": "Đã lưu ghi chú!", "note_id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/notes")
def get_notes(email: str):
    try:
        notes_ref = db.collection("notes")
        query = notes_ref.where("user_email", "==", email).stream()
        
        result = []
        for doc in query:
            note_data = doc.to_dict()
            note_data["id"] = doc.id
            result.append(note_data)
            
        result.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/notes/{note_id}")
def delete_note(note_id: str):
    try:
        doc_ref = db.collection("notes").document(note_id)
        doc_ref.delete()
        
        return {"status": "success", "message": "Đã xóa ghi chú thành công!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))