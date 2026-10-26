# -*- coding: utf-8 -*-
import base64

# Read binary image and convert to clean base64 string (NO BOM)
with open('spongebob_patrick.png', 'rb') as f:
    clean_b64 = base64.b64encode(f.read()).decode('ascii')

print(f"Clean Base64 length: {len(clean_b64)}, starts with: {clean_b64[:20]}")

html_content = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>랜덤 역할 분배기 | 퉷! 셔플 매칭</title>
  <meta name="description" content="유쾌한 '퉷!' 롤링 연출과 함께 공정하게 역할을 분배하는 무작위 1:1 매칭 웹 애플리케이션">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-light: #eef2ff;
      --primary-ring: rgba(79, 70, 229, 0.25);
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --card-border: #e2e8f0;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-light: #94a3b8;
      --radius-lg: 18px;
      --radius-md: 12px;
      --radius-sm: 8px;
      --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.07);
      --shadow-md: 0 4px 16px -2px rgb(0 0 0 / 0.06), 0 2px 6px -1px rgb(0 0 0 / 0.04);
      --shadow-lg: 0 12px 32px -4px rgb(0 0 0 / 0.08), 0 4px 12px -2px rgb(0 0 0 / 0.04);
      --shadow-xl: 0 20px 40px -8px rgb(0 0 0 / 0.12);
      --accent-pink: #f43f5e;
      --accent-yellow: #eab308;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      position: relative;
      background-image: radial-gradient(#cbd5e1 0.75px, transparent 0.75px);
      background-size: 24px 24px;
      overflow-x: hidden;
    }}

    /* Header */
    header {{
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      position: sticky;
      top: 0;
      z-index: 40;
    }}

    .header-inner {{
      max-width: 1040px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .logo-area {{
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      user-select: none;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, #4f46e5, #7c3aed);
      color: white;
      width: 40px;
      height: 40px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
      flex-shrink: 0;
      transition: transform 0.2s ease;
    }}

    .logo-area:hover .logo-badge {{
      transform: scale(1.05) rotate(-4deg);
    }}

    .logo-text {{
      display: flex;
      flex-direction: column;
    }}

    .logo-title {{
      font-size: 1.125rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .logo-tag {{
      font-size: 0.6875rem;
      font-weight: 700;
      background: #eef2ff;
      color: #4f46e5;
      padding: 2px 7px;
      border-radius: 6px;
      letter-spacing: normal;
    }}

    .logo-desc {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .icon-btn {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      transition: all 0.2s ease;
    }}

    .icon-btn:hover {{
      background: var(--bg);
      color: var(--text-main);
      border-color: #cbd5e1;
    }}

    .icon-btn.active {{
      background: #eef2ff;
      color: var(--primary);
      border-color: #c7d2fe;
    }}

    /* Main Container */
    main {{
      max-width: 1040px;
      width: 100%;
      margin: 0 auto;
      padding: 32px 20px 60px;
      flex: 1;
    }}

    /* Section Styling */
    .section-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 32px;
      box-shadow: var(--shadow-md);
      transition: box-shadow 0.25s ease;
    }}

    /* Input View */
    #input-section {{
      display: block;
    }}

    .hero-banner {{
      margin-bottom: 24px;
      text-align: center;
    }}

    .hero-banner h1 {{
      font-size: 1.85rem;
      font-weight: 900;
      color: var(--text-main);
      letter-spacing: -0.03em;
      margin-bottom: 8px;
    }}

    .hero-banner p {{
      color: var(--text-muted);
      font-size: 0.95rem;
      max-width: 600px;
      margin: 0 auto;
    }}

    /* Preset Chips */
    .presets-row {{
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 18px;
    }}

    .presets-label {{
      font-size: 0.8125rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-right: 4px;
    }}

    .preset-chip {{
      background: #f1f5f9;
      border: 1px solid #e2e8f0;
      border-radius: 20px;
      padding: 6px 14px;
      font-size: 0.8125rem;
      font-weight: 600;
      color: #475569;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}

    .preset-chip:hover {{
      background: #e2e8f0;
      color: #0f172a;
      transform: translateY(-1px);
    }}

    /* Grid Inputs */
    .input-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-top: 28px;
    }}

    @media (max-width: 768px) {{
      .input-grid {{
        grid-template-columns: 1fr;
        gap: 20px;
      }}
      .section-card {{
        padding: 20px;
      }}
      .hero-banner h1 {{
        font-size: 1.45rem;
      }}
    }}

    .input-box {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .box-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .box-title {{
      font-size: 0.9375rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .badge-count {{
      font-size: 0.75rem;
      font-weight: 700;
      background: #f1f5f9;
      color: #475569;
      padding: 2px 9px;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
    }}

    .box-actions {{
      display: flex;
      gap: 8px;
    }}

    .sub-action-btn {{
      background: none;
      border: none;
      font-size: 0.75rem;
      color: var(--text-light);
      cursor: pointer;
      padding: 2px 4px;
      transition: color 0.15s;
    }}

    .sub-action-btn:hover {{
      color: var(--accent-pink);
    }}

    .textarea-wrapper {{
      position: relative;
    }}

    textarea {{
      width: 100%;
      height: 190px;
      padding: 14px 16px;
      border: 1.5px solid var(--card-border);
      border-radius: var(--radius-md);
      font-size: 0.9375rem;
      font-family: inherit;
      color: var(--text-main);
      background-color: #fafbfc;
      resize: vertical;
      line-height: 1.6;
      transition: all 0.2s ease;
      outline: none;
    }}

    textarea:focus {{
      border-color: var(--primary);
      background-color: #ffffff;
      box-shadow: 0 0 0 4px var(--primary-ring);
    }}

    textarea::placeholder {{
      color: #94a3b8;
      font-size: 0.875rem;
    }}

    .input-hint {{
      font-size: 0.75rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 4px;
    }}

    /* Notice banner for mismatch rules */
    .status-banner {{
      margin-top: 24px;
      padding: 14px 18px;
      border-radius: var(--radius-md);
      font-size: 0.875rem;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      background: #f8fafc;
      border: 1.5px solid #e2e8f0;
      color: #475569;
      transition: all 0.3s ease;
    }}

    .status-banner.match {{
      background: #f0fdf4;
      border-color: #bbf7d0;
      color: #166534;
    }}

    .status-banner.more-participants {{
      background: #fffbeb;
      border-color: #fde68a;
      color: #92400e;
    }}

    .status-banner.more-roles {{
      background: #eff6ff;
      border-color: #bfdbfe;
      color: #1e40af;
    }}

    .status-icon {{
      font-size: 1.25rem;
      line-height: 1.2;
      flex-shrink: 0;
    }}

    /* Start Button Area */
    .action-row {{
      margin-top: 28px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }}

    .primary-btn {{
      background: linear-gradient(135deg, var(--primary) 0%, #6366f1 100%);
      color: white;
      border: none;
      padding: 16px 42px;
      border-radius: 14px;
      font-size: 1.125rem;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 8px 24px -3px rgba(79, 70, 229, 0.42);
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
      user-select: none;
    }}

    .primary-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 28px -3px rgba(79, 70, 229, 0.52);
    }}

    .primary-btn:active {{
      transform: translateY(1px);
    }}

    .keyboard-shortcut-hint {{
      font-size: 0.75rem;
      color: var(--text-light);
    }}

    /* Draw Stage View */
    #draw-section {{
      display: none;
    }}

    .stage-container {{
      position: relative;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 32px 24px;
      box-shadow: var(--shadow-lg);
      margin-bottom: 24px;
      overflow: hidden;
    }}

    /* Top Action Bar in Result / Stage */
    .stage-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      flex-wrap: wrap;
      gap: 12px;
      padding-bottom: 16px;
      border-bottom: 1px solid #f1f5f9;
    }}

    .stage-status {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .status-indicator {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #eab308;
      display: inline-block;
      animation: pulse 1.5s infinite;
    }}

    .status-indicator.done {{
      background: #10b981;
      animation: none;
    }}

    @keyframes pulse {{
      0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(234, 179, 8, 0.7); }}
      70% {{ transform: scale(1); box-shadow: 0 0 0 8px rgba(234, 179, 8, 0); }}
      100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(234, 179, 8, 0); }}
    }}

    .stage-title {{
      font-size: 1.125rem;
      font-weight: 800;
      color: var(--text-main);
    }}

    .stage-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-secondary {{
      background: #ffffff;
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 9px 16px;
      border-radius: var(--radius-md);
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }}

    .btn-secondary:hover {{
      background: #f8fafc;
      border-color: #cbd5e1;
      transform: translateY(-1px);
    }}

    .btn-secondary:active {{
      transform: translateY(0);
    }}

    .btn-secondary.primary-outline {{
      color: var(--primary);
      border-color: #c7d2fe;
      background: #eef2ff;
    }}

    .btn-secondary.primary-outline:hover {{
      background: #e0e7ff;
      border-color: #a5b4fc;
    }}

    /* Character Cinema Area */
    .character-showcase {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 12px 0 24px;
      position: relative;
    }}

    .character-frame-wrapper {{
      position: relative;
      width: 270px;
      height: 270px;
      border-radius: 28px;
      background: linear-gradient(145deg, #e0f2fe, #fef3c7);
      padding: 8px;
      box-shadow: 0 16px 36px -8px rgba(0, 0, 0, 0.14), 0 0 0 1px rgba(0, 0, 0, 0.05);
      transition: transform 0.2s ease;
    }}

    .character-frame {{
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 20px;
      overflow: hidden;
      background: #ffffff;
    }}

    .character-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      user-select: none;
      -webkit-user-drag: none;
    }}

    /* Comic vibration lines */
    .vibration-lines {{
      position: absolute;
      top: -15px;
      left: -15px;
      right: -15px;
      bottom: -15px;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.2s ease;
    }}

    .character-frame-wrapper.shaking .vibration-lines {{
      opacity: 1;
    }}

    .vibe-line {{
      position: absolute;
      font-size: 1.25rem;
      font-weight: 900;
      color: #f59e0b;
      user-select: none;
      animation: vibePulse 0.15s infinite alternate;
    }}

    @keyframes vibePulse {{
      0% {{ transform: scale(0.9) rotate(-4deg); opacity: 0.6; }}
      100% {{ transform: scale(1.1) rotate(4deg); opacity: 1; }}
    }}

    /* Mouth Points */
    .mouth-anchor {{
      position: absolute;
      width: 16px;
      height: 16px;
      pointer-events: none;
      z-index: 10;
    }}

    /* Left mouth area */
    #mouth-left {{
      left: 26%;
      top: 68%;
    }}

    /* Right mouth area */
    #mouth-right {{
      left: 70%;
      top: 76%;
    }}

    /* Spit Visual Effect Text (퉷!) */
    .spit-burst-text {{
      position: fixed;
      font-size: 1.85rem;
      font-weight: 900;
      color: #f43f5e;
      text-shadow: 0 3px 10px rgba(244, 63, 94, 0.5), 2px 2px 0 #fff, -2px -2px 0 #fff;
      pointer-events: none;
      z-index: 10000;
      animation: burstPop 0.55s ease-out forwards;
      transform: translate(-50%, -50%);
      white-space: nowrap;
    }}

    @keyframes burstPop {{
      0% {{ opacity: 0; transform: translate(-50%, -50%) scale(0.4) rotate(-15deg); }}
      30% {{ opacity: 1; transform: translate(-50%, -85%) scale(1.35) rotate(6deg); }}
      70% {{ opacity: 0.9; transform: translate(-50%, -105%) scale(1.1) rotate(0deg); }}
      100% {{ opacity: 0; transform: translate(-50%, -125%) scale(0.7) rotate(12deg); }}
    }}

    /* Shake Keyframes */
    .shaking {{
      animation: intenseShake 0.1s infinite;
    }}

    @keyframes intenseShake {{
      0% {{ transform: translate(0, 0) rotate(0deg) scale(1); }}
      20% {{ transform: translate(-4px, 3px) rotate(-2deg) scale(1.03); }}
      40% {{ transform: translate(4px, -3px) rotate(2deg) scale(1.02); }}
      60% {{ transform: translate(-3px, -2px) rotate(-1.5deg) scale(1.04); }}
      80% {{ transform: translate(3px, 3px) rotate(1.5deg) scale(1.02); }}
      100% {{ transform: translate(0, 0) rotate(0deg) scale(1); }}
    }}

    /* Dramatic Action Message */
    .stage-subtitle {{
      margin-top: 18px;
      font-size: 1.0625rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
      text-align: center;
      min-height: 28px;
    }}

    .sub-indicator-badge {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      background: #eef2ff;
      color: var(--primary);
      padding: 3px 10px;
      border-radius: 12px;
      letter-spacing: -0.01em;
    }}

    /* Flying Projectile Badge */
    .flying-badge {{
      position: fixed;
      z-index: 9999;
      background: linear-gradient(135deg, #4f46e5, #7c3aed);
      color: white;
      font-weight: 800;
      font-size: 0.9375rem;
      padding: 8px 20px;
      border-radius: 20px;
      box-shadow: 0 10px 25px -3px rgba(79, 70, 229, 0.6), 0 0 0 2px rgba(255, 255, 255, 0.85);
      pointer-events: none;
      white-space: nowrap;
      transition: transform 0.44s cubic-bezier(0.2, 0.9, 0.3, 1.2), opacity 0.44s ease;
      will-change: transform, opacity;
    }}

    /* Matching Result Grid */
    .matching-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin-top: 16px;
    }}

    @media (max-width: 680px) {{
      .matching-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Slot Card */
    .slot-card {{
      background: #ffffff;
      border: 1.5px solid var(--card-border);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      box-shadow: var(--shadow-sm);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
    }}

    .slot-card.waiting-mode {{
      background: #f8fafc;
      border-style: dashed;
    }}

    .slot-card.locked {{
      border-color: #c7d2fe;
      background: #ffffff;
      box-shadow: 0 4px 14px -1px rgba(79, 70, 229, 0.08);
    }}

    .slot-card.just-snapped {{
      animation: snapLanding 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      border-color: var(--primary);
    }}

    @keyframes snapLanding {{
      0% {{
        transform: scale(1.06);
        box-shadow: 0 0 0 6px rgba(79, 70, 229, 0.25), 0 12px 24px rgba(79, 70, 229, 0.15);
      }}
      100% {{
        transform: scale(1);
        box-shadow: var(--shadow-sm);
      }}
    }}

    .slot-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
      flex: 1;
    }}

    .slot-index {{
      width: 28px;
      height: 28px;
      border-radius: 8px;
      background: #f1f5f9;
      color: #64748b;
      font-size: 0.8125rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .slot-card.locked .slot-index {{
      background: #eef2ff;
      color: var(--primary);
    }}

    /* Participant Name Box (Target of projectile) */
    .slot-participant-target {{
      position: relative;
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      padding: 4px 10px;
      border-radius: 8px;
      min-width: 80px;
    }}

    /* Rolling animation inside the slot */
    .slot-participant-target.rolling {{
      color: #6366f1;
      background: #eef2ff;
      animation: slotRollingGlow 0.35s infinite alternate ease-in-out;
    }}

    @keyframes slotRollingGlow {{
      0% {{ opacity: 0.6; transform: translateY(-1.5px); }}
      100% {{ opacity: 1; transform: translateY(1.5px); }}
    }}

    .slot-arrow {{
      color: #94a3b8;
      font-size: 1rem;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: color 0.2s ease;
    }}

    .slot-card.locked .slot-arrow {{
      color: var(--primary);
    }}

    .slot-right {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }}

    .role-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #f1f5f9;
      color: #334155;
      font-size: 0.875rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid #e2e8f0;
      max-width: 180px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .role-badge.waiting {{
      background: #f8fafc;
      color: #64748b;
      border-color: #cbd5e1;
      font-weight: 600;
    }}

    .role-badge.assigned {{
      background: #f0fdf4;
      color: #166534;
      border-color: #bbf7d0;
    }}

    /* Confetti Canvas */
    #confetti-canvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 999;
    }}

    /* Toast Notification */
    .toast-container {{
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10000;
      display: flex;
      flex-direction: column;
      gap: 8px;
      align-items: center;
      pointer-events: none;
    }}

    .toast {{
      background: rgba(15, 23, 42, 0.94);
      backdrop-filter: blur(8px);
      color: white;
      padding: 12px 22px;
      border-radius: 30px;
      font-size: 0.875rem;
      font-weight: 600;
      box-shadow: var(--shadow-xl);
      display: flex;
      align-items: center;
      gap: 8px;
      opacity: 0;
      transform: translateY(12px) scale(0.95);
      animation: toastIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      pointer-events: auto;
    }}

    @keyframes toastIn {{
      to {{
        opacity: 1;
        transform: translateY(0) scale(1);
      }}
    }}

    .toast.out {{
      animation: toastOut 0.25s ease forwards;
    }}

    @keyframes toastOut {{
      to {{
        opacity: 0;
        transform: translateY(-8px) scale(0.95);
      }}
    }}

    /* Footer */
    footer {{
      text-align: center;
      padding: 24px;
      color: var(--text-light);
      font-size: 0.8125rem;
      margin-top: auto;
    }}
  </style>
</head>
<body>

  <!-- Confetti Canvas -->
  <canvas id="confetti-canvas"></canvas>

  <!-- Header -->
  <header>
    <div class="header-inner">
      <div class="logo-area" onclick="returnToEdit()">
        <div class="logo-badge">🎲</div>
        <div class="logo-text">
          <div class="logo-title">
            랜덤 역할 분배기
            <span class="logo-tag">퉷! 셔플</span>
          </div>
          <span class="logo-desc">공정하고 빠른 1:1 무작위 매칭</span>
        </div>
      </div>
      <div class="header-actions">
        <button id="sound-toggle-btn" class="icon-btn active" title="사운드 효과 켜기/끄기">
          <span id="sound-icon">🔊</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <!-- View 1: Input Section -->
    <section id="input-section" class="section-card">
      <div class="hero-banner">
        <h1>누가 어떤 역할을 맡을까요?</h1>
        <p>참가자 명단과 역할을 입력하고, 시원한 '퉷!' 추첨으로 빠르게 배정하세요.</p>
        
        <!-- Quick Presets -->
        <div class="presets-row">
          <span class="presets-label">⚡ 빠른 예시:</span>
          <button type="button" class="preset-chip" onclick="loadPreset('team')">💻 팀 프로젝트</button>
          <button type="button" class="preset-chip" onclick="loadPreset('study')">📚 스터디/회의</button>
          <button type="button" class="preset-chip" onclick="loadPreset('dinner')">🍽 회식/야식 내기</button>
          <button type="button" class="preset-chip" onclick="loadPreset('game')">🎮 게임/보드게임</button>
        </div>
      </div>

      <!-- Input Grids -->
      <div class="input-grid">
        <!-- Participants Input -->
        <div class="input-box">
          <div class="box-header">
            <label for="participants-input" class="box-title">
              <span>👤 참가자 명단</span>
              <span id="participants-count" class="badge-count">0명</span>
            </label>
            <div class="box-actions">
              <button type="button" class="sub-action-btn" onclick="clearInput('participants-input')">지우기</button>
            </div>
          </div>
          <div class="textarea-wrapper">
            <textarea id="participants-input" placeholder="참가자 이름을 입력하세요.&#10;(줄바꿈 또는 쉼표로 구분)&#10;&#10;예시:&#10;김민수, 이영희, 박철수, 최유진, 정수빈" spellcheck="false"></textarea>
          </div>
          <div class="input-hint">
            <span>엔터(줄바꿈)나 쉼표(,)로 구분</span>
            <span id="participant-validation"></span>
          </div>
        </div>

        <!-- Roles Input -->
        <div class="input-box">
          <div class="box-header">
            <label for="roles-input" class="box-title">
              <span>🎯 역할 목록</span>
              <span id="roles-count" class="badge-count">0개</span>
            </label>
            <div class="box-actions">
              <button type="button" class="sub-action-btn" onclick="clearInput('roles-input')">지우기</button>
            </div>
          </div>
          <div class="textarea-wrapper">
            <textarea id="roles-input" placeholder="배정할 역할을 입력하세요.&#10;(줄바꿈 또는 쉼표로 구분)&#10;&#10;예시:&#10;팀장, 프론트엔드, 백엔드, UI/UX 디자인" spellcheck="false"></textarea>
          </div>
          <div class="input-hint">
            <span>엔터(줄바꿈)나 쉼표(,)로 구분</span>
            <span id="role-validation"></span>
          </div>
        </div>
      </div>

      <!-- Rule Notice Banner -->
      <div id="status-banner" class="status-banner">
        <span class="status-icon">💡</span>
        <span id="status-text">참가자와 역할을 입력하시면 실시간 매칭 상태를 확인해 드립니다.</span>
      </div>

      <!-- Submit Action -->
      <div class="action-row">
        <button id="start-btn" class="primary-btn" onclick="startDrawProcess()">
          <span>역할 매칭 시작</span>
          <span style="font-size: 1.25rem;">➔</span>
        </button>
        <span class="keyboard-shortcut-hint">단축키: Ctrl + Enter</span>
      </div>
    </section>

    <!-- View 2: Draw Animation & Result Section -->
    <section id="draw-section">
      <div class="stage-container">
        
        <!-- Stage Controls / Header -->
        <div class="stage-header">
          <div class="stage-status">
            <span id="stage-indicator" class="status-indicator"></span>
            <span id="stage-title-text" class="stage-title">역할 추첨 진행 중...</span>
          </div>
          <div class="stage-controls">
            <button id="skip-btn" class="btn-secondary" onclick="skipDrawAnimation()">
              ⏩ 즉시 확인
            </button>
            <button id="copy-btn" class="btn-secondary primary-outline" onclick="copyResultsToClipboard()" style="display: none;">
              📋 결과 복사
            </button>
            <button id="retry-btn" class="btn-secondary" onclick="retryDraw()" style="display: none;">
              🔄 다시 뽑기
            </button>
            <button id="edit-btn" class="btn-secondary" onclick="returnToEdit()" style="display: none;">
              ✏️ 명단 수정
            </button>
          </div>
        </div>

        <!-- Cinema Character Stage -->
        <div class="character-showcase">
          <div id="character-wrapper" class="character-frame-wrapper">
            <!-- Comic vibration lines around the characters -->
            <div class="vibration-lines">
              <span class="vibe-line" style="top: 10px; left: -14px;">彡</span>
              <span class="vibe-line" style="top: 80px; left: -18px;">彡</span>
              <span class="vibe-line" style="bottom: 40px; left: -14px;">彡</span>
              <span class="vibe-line" style="top: 10px; right: -14px;">ミ</span>
              <span class="vibe-line" style="top: 80px; right: -18px;">ミ</span>
              <span class="vibe-line" style="bottom: 40px; right: -14px;">ミ</span>
            </div>
            <div class="character-frame">
              <img id="draw-character-img" class="character-img" src="data:image/png;base64,{clean_b64}" onerror="this.onerror=null; this.src='spongebob_patrick.png';" alt="">
              <!-- Anchors for mouth locations -->
              <div id="mouth-left" class="mouth-anchor"></div>
              <div id="mouth-right" class="mouth-anchor"></div>
            </div>
          </div>
          <div id="stage-action-text" class="stage-subtitle">
            <span class="sub-indicator-badge">추첨 연출</span>
            <span id="action-desc-message">추첨을 위해 심호흡 중입니다...! (덜덜덜)</span>
          </div>
        </div>

        <!-- Slots / Results Grid -->
        <div id="matching-grid" class="matching-grid">
          <!-- Dynamically populated slots -->
        </div>

      </div>
    </section>
  </main>

  <!-- Toast Container -->
  <div id="toast-container" class="toast-container"></div>

  <footer>
    <p>100% 무가중치 공정 1:1 셔플 매칭 시스템 • 단일 파일 동작 웹 애플리케이션</p>
  </footer>

  <script>
    /* =========================================================================
       1. Presets & State
       ========================================================================= */
    const presets = {{
      team: {{
        participants: "김민수\\n이영희\\n박철수\\n최유진\\n정수빈",
        roles: "👑 팀장 / 기획\\n💻 프론트엔드 개발\\n🛠 백엔드 개발\\n🎨 UI/UX 디자인"
      }},
      study: {{
        participants: "강지훈\\n조혜린\\n윤도현\\n서예은",
        roles: "📖 1장 발제자\\n📝 회의록 서기\\n⏰ 타임키퍼\\n☕ 다과 담당"
      }},
      dinner: {{
        participants: "팀장님\\n이과장\\n박대리\\n최사원\\n정인턴",
        roles: "💳 법카 결제자\\n📍 식당 예약러\\n🚗 운전자\\n🥢 수저 세팅러"
      }},
      game: {{
        participants: "아서\\n멀린\\n모드레드\\n퍼시벌\\n모르가나",
        roles: "🛡️ 수호 기사\\n🧙‍♂️ 대마법사\\n🗡️ 암살자\\n🏹 궁수"
      }}
    }};

    let isSoundEnabled = true;
    let isDrawing = false;
    let skipRequested = false;
    let currentMatches = [];
    let audioCtx = null;

    /* =========================================================================
       2. Web Audio API Sound Synthesizer (No external sound files required)
       ========================================================================= */
    function getAudioContext() {{
      if (!audioCtx) {{
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (AudioContextClass) {{
          audioCtx = new AudioContextClass();
        }}
      }}
      if (audioCtx && audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
      return audioCtx;
    }}

    // Mute toggle
    document.getElementById('sound-toggle-btn').addEventListener('click', () => {{
      isSoundEnabled = !isSoundEnabled;
      const btn = document.getElementById('sound-toggle-btn');
      const icon = document.getElementById('sound-icon');
      if (isSoundEnabled) {{
        btn.classList.add('active');
        icon.textContent = '🔊';
        showToast('🔊 효과음이 켜졌습니다.');
        playSnapSound();
      }} else {{
        btn.classList.remove('active');
        icon.textContent = '🔇';
        showToast('🔇 효과음이 꺼졌습니다.');
      }}
    }});

    // Rolling Tick Sound
    function playTickSound() {{
      if (!isSoundEnabled) return;
      try {{
        const ctx = getAudioContext();
        if (!ctx) return;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(520 + Math.random() * 140, ctx.currentTime);
        gain.gain.setValueAtTime(0.04, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.04);
      }} catch (e) {{}}
    }}

    // Spit / Poot! Sound (퉷! 소리 - 내려가는 글리산도 귀여운 팝)
    function playSpitSound() {{
      if (!isSoundEnabled) return;
      try {{
        const ctx = getAudioContext();
        if (!ctx) return;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        const now = ctx.currentTime;
        osc.frequency.setValueAtTime(880, now);
        osc.frequency.exponentialRampToValueAtTime(180, now + 0.16);
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.16);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.16);
      }} catch (e) {{}}
    }}

    // Snap / Landing Sound (찰칵! 착지 사운드)
    function playSnapSound() {{
      if (!isSoundEnabled) return;
      try {{
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        [587.33, 880, 1174.66].forEach((freq, idx) => {{
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + idx * 0.02);
          gain.gain.setValueAtTime(0.12, now + idx * 0.02);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.02 + 0.14);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + idx * 0.02);
          osc.stop(now + idx * 0.02 + 0.14);
        }});
      }} catch (e) {{}}
    }}

    // Fanfare Sound (완료 축하 화음)
    function playFanfareSound() {{
      if (!isSoundEnabled) return;
      try {{
        const ctx = getAudioContext();
        if (!ctx) return;
        const now = ctx.currentTime;
        const notes = [523.25, 659.25, 783.99, 1046.50];
        notes.forEach((freq, i) => {{
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + i * 0.08);
          gain.gain.setValueAtTime(0.15, now + i * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.35);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.08);
          osc.stop(now + i * 0.08 + 0.35);
        }});
      }} catch (e) {{}}
    }}

    /* =========================================================================
       3. Input Handling & Real-time Feedback
       ========================================================================= */
    const participantsInput = document.getElementById('participants-input');
    const rolesInput = document.getElementById('roles-input');
    const participantsCount = document.getElementById('participants-count');
    const rolesCount = document.getElementById('roles-count');
    const statusBanner = document.getElementById('status-banner');
    const statusText = document.getElementById('status-text');

    function parseItems(text) {{
      if (!text) return [];
      return text
        .split(/[\\n,]+/)
        .map(item => item.trim())
        .filter(item => item.length > 0);
    }}

    function updateInputStatus() {{
      const pList = parseItems(participantsInput.value);
      const rList = parseItems(rolesInput.value);
      const pCount = pList.length;
      const rCount = rList.length;

      participantsCount.textContent = `${{pCount}}명`;
      rolesCount.textContent = `${{rCount}}개`;

      // Status Banner update
      statusBanner.className = 'status-banner';
      if (pCount === 0 && rCount === 0) {{
        statusText.innerHTML = '참가자와 역할을 입력하시면 실시간 매칭 상태를 확인해 드립니다.';
      }} else if (pCount === 0) {{
        statusText.innerHTML = '⚠️ 참가자 이름을 입력해 주세요.';
      }} else if (rCount === 0) {{
        statusText.innerHTML = '⚠️ 배정할 역할을 1개 이상 입력해 주세요.';
      }} else if (pCount === rCount) {{
        statusBanner.classList.add('match');
        statusText.innerHTML = `<strong>✨ 완벽한 1:1 매칭:</strong> 참가자 ${{pCount}}명과 역할 ${{rCount}}개가 정확히 일치합니다!`;
      }} else if (pCount > rCount) {{
        statusBanner.classList.add('more-participants');
        const diff = pCount - rCount;
        statusText.innerHTML = `<strong>👥 참가자 초과 (${{pCount}}명 > ${{rCount}}개):</strong> 역할 배정 후 남는 <strong>${{diff}}명</strong>은 자동으로 <strong>'대기/서포트'</strong>로 배정됩니다.`;
      }} else {{
        statusBanner.classList.add('more-roles');
        const diff = rCount - pCount;
        statusText.innerHTML = `<strong>🎯 역할 초과 (${{rCount}}개 > ${{pCount}}명):</strong> 전체 ${{rCount}}개 역할 중 참가자 수에 맞춰 <strong>${{pCount}}개</strong>만 무작위 선정되어 배정됩니다.`;
      }}
    }}

    participantsInput.addEventListener('input', updateInputStatus);
    rolesInput.addEventListener('input', updateInputStatus);

    // Keyboard Shortcuts: Ctrl+Enter / Cmd+Enter to Start
    window.addEventListener('keydown', (e) => {{
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {{
        e.preventDefault();
        if (inputSection.style.display !== 'none') {{
          startDrawProcess();
        }}
      }}
      if (e.key === 'Escape') {{
        if (drawSection.style.display !== 'none' && !isDrawing) {{
          returnToEdit();
        }}
      }}
    }});

    function clearInput(id) {{
      document.getElementById(id).value = '';
      updateInputStatus();
      document.getElementById(id).focus();
    }}

    function loadPreset(key) {{
      const data = presets[key];
      if (data) {{
        participantsInput.value = data.participants;
        rolesInput.value = data.roles;
        updateInputStatus();
        showToast('⚡ 예시 데이터가 입력되었습니다.');
      }}
    }}

    /* =========================================================================
       4. Matching Algorithm (Single 1:1 Shuffle Matching)
       ========================================================================= */
    function shuffleArray(arr) {{
      const shuffled = [...arr];
      for (let i = shuffled.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
      }}
      return shuffled;
    }}

    function executeRoleMatching(participants, roles) {{
      const shuffledParticipants = shuffleArray(participants);
      const shuffledRoles = shuffleArray(roles);
      const matches = [];

      const pCount = shuffledParticipants.length;
      const rCount = shuffledRoles.length;

      if (pCount <= rCount) {{
        // 역할이 더 많거나 같은 경우: 참가자 수만큼 역할 배정
        for (let i = 0; i < pCount; i++) {{
          matches.push({{
            index: i + 1,
            participant: shuffledParticipants[i],
            role: shuffledRoles[i],
            isWaiting: false
          }});
        }}
      }} else {{
        // 참가자가 더 많은 경우: 역할 수만큼 배정 후 남은 참가자는 '대기/서포트'
        for (let i = 0; i < rCount; i++) {{
          matches.push({{
            index: i + 1,
            participant: shuffledParticipants[i],
            role: shuffledRoles[i],
            isWaiting: false
          }});
        }}
        for (let i = rCount; i < pCount; i++) {{
          matches.push({{
            index: i + 1,
            participant: shuffledParticipants[i],
            role: '대기/서포트',
            isWaiting: true
          }});
        }}
      }}

      return matches;
    }}

    /* =========================================================================
       5. Animation & Draw Process
       ========================================================================= */
    const inputSection = document.getElementById('input-section');
    const drawSection = document.getElementById('draw-section');
    const matchingGrid = document.getElementById('matching-grid');
    const characterWrapper = document.getElementById('character-wrapper');
    const stageIndicator = document.getElementById('stage-indicator');
    const stageTitleText = document.getElementById('stage-title-text');
    const actionDescMessage = document.getElementById('action-desc-message');
    const skipBtn = document.getElementById('skip-btn');
    const copyBtn = document.getElementById('copy-btn');
    const retryBtn = document.getElementById('retry-btn');
    const editBtn = document.getElementById('edit-btn');
    const mouthLeft = document.getElementById('mouth-left');
    const mouthRight = document.getElementById('mouth-right');

    function startDrawProcess() {{
      const participants = parseItems(participantsInput.value);
      const roles = parseItems(rolesInput.value);

      if (participants.length === 0) {{
        showToast('⚠️ 참가자 이름을 먼저 1명 이상 입력해 주세요.');
        participantsInput.focus();
        return;
      }}
      if (roles.length === 0) {{
        showToast('⚠️ 배정할 역할을 먼저 1개 이상 입력해 주세요.');
        rolesInput.focus();
        return;
      }}

      // Init Web Audio on user gesture
      getAudioContext();

      // Execute Algorithm
      currentMatches = executeRoleMatching(participants, roles);
      skipRequested = false;
      isDrawing = true;

      // Switch View
      inputSection.style.display = 'none';
      drawSection.style.display = 'block';
      window.scrollTo({{ top: 0, behavior: 'smooth' }});

      // Reset Stage Controls
      skipBtn.style.display = 'inline-flex';
      copyBtn.style.display = 'none';
      retryBtn.style.display = 'none';
      editBtn.style.display = 'none';
      stageIndicator.className = 'status-indicator';
      stageTitleText.textContent = '역할 추첨 진행 중...';

      // Build Initial Slots
      renderInitialSlots(currentMatches);

      // Run Choreographed Animation
      runFullDrawAnimation(participants);
    }}

    function renderInitialSlots(matches) {{
      matchingGrid.innerHTML = '';
      matches.forEach((item, idx) => {{
        const card = document.createElement('div');
        card.id = `slot-${{idx}}`;
        card.className = `slot-card ${{item.isWaiting ? 'waiting-mode' : ''}}`;
        card.innerHTML = `
          <div class="slot-left">
            <div class="slot-index">${{item.index}}</div>
            <div id="target-name-${{idx}}" class="slot-participant-target rolling">
              추첨 대기 중...
            </div>
            <div class="slot-arrow">➔</div>
          </div>
          <div class="slot-right">
            <span class="role-badge ${{item.isWaiting ? 'waiting' : ''}}">
              ${{item.role}}
            </span>
          </div>
        `;
        matchingGrid.appendChild(card);
      }});
    }}

    async function runFullDrawAnimation(participants) {{
      // Phase 1: Intense Shake + Text Rolling (1.8s)
      characterWrapper.classList.add('shaking');
      actionDescMessage.textContent = '추첨을 위해 심호흡 중입니다...! (덜덜덜)';

      let rollInterval = setInterval(() => {{
        playTickSound();
        currentMatches.forEach((_, idx) => {{
          const target = document.getElementById(`target-name-${{idx}}`);
          if (target && target.classList.contains('rolling')) {{
            const randomName = participants[Math.floor(Math.random() * participants.length)];
            target.textContent = randomName;
          }}
        }});
      }}, 50);

      await sleep(1800);
      clearInterval(rollInterval);

      if (skipRequested) {{
        finalizeDrawInstantly();
        return;
      }}

      // Phase 2: Sequential Spit & Drop! (입에서 하나씩 퉷! 뱉어져 착지)
      actionDescMessage.innerHTML = '<strong>퉷!</strong> 참가자가 뿜어져 나와 역할에 찰칵 꽂힙니다!';

      for (let i = 0; i < currentMatches.length; i++) {{
        if (skipRequested) break;

        const match = currentMatches[i];
        const isLeft = (i % 2 === 0);
        const sourceMouth = isLeft ? mouthLeft : mouthRight;

        actionDescMessage.textContent = `'${{match.participant}}' 발사! 퉷!`;

        // Create '퉷!' cartoon burst text at mouth
        showSpitBurst(sourceMouth);
        playSpitSound();

        // Animate Flying Projectile Badge
        await animateFlyingSpit(sourceMouth, i, match.participant);

        // Snap Target
        snapSlotIntoPlace(i, match);
        playSnapSound();

        // Brief dramatic pause before next spit
        await sleep(350);
      }}

      // Phase 3: Finish
      characterWrapper.classList.remove('shaking');
      finishDrawProcess();
    }}

    function showSpitBurst(mouthElem) {{
      const rect = mouthElem.getBoundingClientRect();
      const burst = document.createElement('div');
      burst.className = 'spit-burst-text';
      burst.textContent = '퉷!!';
      burst.style.left = `${{rect.left + rect.width / 2}}px`;
      burst.style.top = `${{rect.top + rect.height / 2}}px`;
      document.body.appendChild(burst);
      setTimeout(() => burst.remove(), 600);
    }}

    function animateFlyingSpit(mouthElem, slotIdx, participantName) {{
      return new Promise(resolve => {{
        const targetElem = document.getElementById(`target-name-${{slotIdx}}`);
        if (!targetElem || skipRequested) {{
          resolve();
        }}

        const mouthRect = mouthElem.getBoundingClientRect();
        const targetRect = targetElem.getBoundingClientRect();

        const badge = document.createElement('div');
        badge.className = 'flying-badge';
        badge.textContent = participantName;
        badge.style.left = `${{mouthRect.left}}px`;
        badge.style.top = `${{mouthRect.top}}px`;
        badge.style.transform = 'translate(-50%, -50%) scale(0.4)';
        badge.style.opacity = '0.9';
        document.body.appendChild(badge);

        // Force reflow
        badge.offsetHeight;

        // Calculate travel delta
        const deltaX = (targetRect.left + targetRect.width / 2) - mouthRect.left;
        const deltaY = (targetRect.top + targetRect.height / 2) - mouthRect.top;

        badge.style.transform = `translate(calc(-50% + ${{deltaX}}px), calc(-50% + ${{deltaY}}px)) scale(1)`;

        setTimeout(() => {{
          badge.remove();
          resolve();
        }}, 440);
      }});
    }}

    function snapSlotIntoPlace(idx, match) {{
      const card = document.getElementById(`slot-${{idx}}`);
      const target = document.getElementById(`target-name-${{idx}}`);
      if (!card || !target) return;

      target.classList.remove('rolling');
      target.textContent = match.participant;
      card.classList.add('locked', 'just-snapped');

      const roleBadge = card.querySelector('.role-badge');
      if (roleBadge) {{
        roleBadge.classList.add('assigned');
      }}
    }}

    function skipDrawAnimation() {{
      skipRequested = true;
      finalizeDrawInstantly();
    }}

    function finalizeDrawInstantly() {{
      characterWrapper.classList.remove('shaking');
      currentMatches.forEach((match, idx) => {{
        snapSlotIntoPlace(idx, match);
      }});
      playSnapSound();
      finishDrawProcess();
    }}

    function finishDrawProcess() {{
      isDrawing = false;
      stageIndicator.classList.add('done');
      stageTitleText.textContent = '🎉 역할 분배 완료!';
      actionDescMessage.innerHTML = '✨ 모든 역할이 공정하게 1:1로 매칭되었습니다!';

      skipBtn.style.display = 'none';
      copyBtn.style.display = 'inline-flex';
      retryBtn.style.display = 'inline-flex';
      editBtn.style.display = 'inline-flex';

      // Confetti & Fanfare
      triggerConfetti();
      playFanfareSound();
    }}

    function retryDraw() {{
      startDrawProcess();
    }}

    function returnToEdit() {{
      drawSection.style.display = 'none';
      inputSection.style.display = 'block';
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function sleep(ms) {{
      return new Promise(resolve => setTimeout(resolve, ms));
    }}

    /* =========================================================================
       6. Clipboard Copy
       ========================================================================= */
    function copyResultsToClipboard() {{
      if (currentMatches.length === 0) return;

      const lines = [
        '🎲 [랜덤 역할 분배 결과]',
        '-------------------------'
      ];

      currentMatches.forEach(item => {{
        lines.push(`${{item.index}}. ${{item.participant}} ➔ ${{item.role}}`);
      }});

      lines.push('-------------------------');
      lines.push(`(총 ${{currentMatches.length}}명 매칭 완료)`);

      const textToCopy = lines.join('\\n');

      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(textToCopy).then(() => {{
          showToast('📋 결과가 클립보드에 복사되었습니다!');
        }}).catch(() => {{
          fallbackCopyText(textToCopy);
        }});
      }} else {{
        fallbackCopyText(textToCopy);
      }}
    }}

    function fallbackCopyText(text) {{
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try {{
        document.execCommand('copy');
        showToast('📋 결과가 클립보드에 복사되었습니다!');
      }} catch (err) {{
        showToast('⚠️ 복사에 실패했습니다. 수동으로 복사해 주세요.');
      }}
      document.body.removeChild(ta);
    }}

    /* =========================================================================
       7. Toast Notifications
       ========================================================================= */
    function showToast(message) {{
      const container = document.getElementById('toast-container');
      const toast = document.createElement('div');
      toast.className = 'toast';
      toast.textContent = message;
      container.appendChild(toast);

      setTimeout(() => {{
        toast.classList.add('out');
        setTimeout(() => toast.remove(), 250);
      }}, 2400);
    }}

    /* =========================================================================
       8. Canvas Confetti Effect
       ========================================================================= */
    function triggerConfetti() {{
      const canvas = document.getElementById('confetti-canvas');
      const ctx = canvas.getContext('2d');
      const width = canvas.width = window.innerWidth;
      const height = canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#4f46e5', '#6366f1', '#eab308', '#f43f5e', '#10b981', '#06b6d4', '#f97316'];

      for (let i = 0; i < 90; i++) {{
        particles.push({{
          x: width / 2,
          y: height / 2.5,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 0.8) * 16,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          vRot: (Math.random() - 0.5) * 10,
          opacity: 1
        }});
      }}

      let animationFrame;
      function render() {{
        ctx.clearRect(0, 0, width, height);
        let alive = false;

        particles.forEach(p => {{
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.38; // gravity
          p.vx *= 0.98;
          p.rotation += p.vRot;
          p.opacity -= 0.012;

          if (p.opacity > 0) {{
            alive = true;
            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate((p.rotation * Math.PI) / 180);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = Math.max(0, p.opacity);
            ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
            ctx.restore();
          }}
        }});

        if (alive) {{
          animationFrame = requestAnimationFrame(render);
        }} else {{
          ctx.clearRect(0, 0, width, height);
          cancelAnimationFrame(animationFrame);
        }}
      }}

      render();
    }}

    // Resize canvas
    window.addEventListener('resize', () => {{
      const canvas = document.getElementById('confetti-canvas');
      if (canvas) {{
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }}
    }});

    // Initialize with default preset
    loadPreset('team');
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS: index.html generated cleanly without BOM and without character name text!")
