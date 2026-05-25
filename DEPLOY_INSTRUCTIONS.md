# 📦 Guía de Despliegue en Render

## Preparación completada ✅

Tu proyecto Aurora VIP está listo para desplegarse en Render. Aquí están los pasos:

---

## PASO 1: Crear cuenta en Render
1. Ve a https://render.com
2. Regístrate con tu cuenta de GitHub o email
3. Conecta tu repositorio de GitHub

---

## PASO 2: Subir proyecto a GitHub

### Si no tienes Git instalado:
```bash
# Descargar desde https://git-scm.com/download/win
```

### Pasos para subir:

1. **Abre PowerShell en la carpeta del proyecto:**
```bash
cd c:\Users\marti\Desktop\mocads
```

2. **Inicializar Git:**
```bash
git init
git add .
git commit -m "Initial commit: Aurora VIP mockup"
```

3. **Agregar remoto (reemplaza con tu URL de GitHub):**
```bash
git remote add origin https://github.com/TU_USUARIO/aurora-vip.git
git branch -M main
git push -u origin main
```

---

## PASO 3: Crear servicio en Render

1. **Accede a Render Dashboard:** https://dashboard.render.com

2. **Click en "+ New +"** → Selecciona **"Web Service"**

3. **Conecta tu repositorio de GitHub:**
   - Busca "aurora-vip" (o tu repo)
   - Click en "Connect"

4. **Configura el servicio:**
   - **Name:** `aurora-vip` (o el nombre que prefieras)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Plan:** Free (o Starter si quieres mejor rendimiento)

5. **Click en "Create Web Service"**

---

## PASO 4: Variables de Entorno (Opcional)

Si necesitas agregar variables de entorno en Render:

1. Ve a tu servicio en el Dashboard
2. Click en **"Environment"**
3. Agrega variables si es necesario (actualmente no se requieren)

---

## PASO 5: Monitorear el Despliegue

1. En el Dashboard, verás el estado de tu deploy
2. La consola mostrará los logs de construcción
3. Cuando veas ✓ "Build successful", tu app está en línea

Tu URL será similar a:
```
https://aurora-vip.onrender.com
```

---

## Archivos Creados

✅ **Procfile** - Indica a Render cómo ejecutar la app
✅ **runtime.txt** - Especifica la versión de Python
✅ **render.yaml** - Configuración específica de Render
✅ **requirements.txt** - Dependencias actualizadas
✅ **.gitignore** - Archivos a ignorar en Git

---

## Comandos Git Útiles

### Para actualizar después de cambios:
```bash
git add .
git commit -m "Descripción del cambio"
git push origin main
```

### Ver estado actual:
```bash
git status
git log
```

---

## Solución de Problemas

### Si el deploy falla:
1. Revisa los **Logs** en el Dashboard de Render
2. Verifica que `requirements.txt` esté actualizado
3. Asegúrate de que `app.py` tenga la línea:
   ```python
   port = int(os.environ.get("PORT", 5000))
   ```

### Si la app se cae frecuentemente:
- Render free tier reinicia a las 15 min inactivo
- Considera upgrade a plan Starter

---

## URLs Importantes

- 🌐 **Dashboard Render:** https://dashboard.render.com
- 📚 **Documentación:** https://render.com/docs
- 🔗 **Tu App URL:** https://aurora-vip.onrender.com (después del deploy)

---

## ¿Listo para desplegar? ✨

**Próximo paso:** Sube el proyecto a GitHub y crea el servicio en Render.
