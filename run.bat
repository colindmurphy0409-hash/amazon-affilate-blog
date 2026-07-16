@echo off
REM Wellth Lab Amazon Affiliate — one-command helpers (Windows)

if "%1"=="install" (
  pip install -r requirements.txt
  exit /b %ERRORLEVEL%
)

if "%1"=="affiliate-link" (
  if "%2"=="--all" (
    python scripts/build_affiliate_link.py --all
  ) else (
    python scripts/build_affiliate_link.py %2
  )
  exit /b %ERRORLEVEL%
)

if "%1"=="affiliate-validate" (
  python scripts/validate_affiliate_page.py
  exit /b %ERRORLEVEL%
)

if "%1"=="affiliate-dev" (
  cd site && npm run dev
  exit /b %ERRORLEVEL%
)

if "%1"=="affiliate-build" (
  cd site && npm run build
  exit /b %ERRORLEVEL%
)

if "%1"=="affiliate-install" (
  cd site && npm install
  exit /b %ERRORLEVEL%
)

echo.
echo  Wellth Lab Amazon Affiliate Commands
echo  ===================================
echo   run install            Install Python deps (once)
echo   run affiliate-install  Install Astro site deps (once)
echo   run affiliate-link     Build affiliate URL (pass ASIN or --all)
echo   run affiliate-validate Compliance + SEO validation
echo   run affiliate-dev      Astro dev server
echo   run affiliate-build    Production build to site/dist/
echo.
echo  Live site: https://amazon-affilate-blog.vercel.app
echo.
exit /b 0
