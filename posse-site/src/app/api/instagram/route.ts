import { NextResponse } from "next/server";

// Espera as envs: IG_ACCESS_TOKEN e (opcional) IG_USER_ID
// Documentação: https://developers.facebook.com/docs/instagram-basic-display-api

export async function GET() {
  const accessToken = process.env.IG_ACCESS_TOKEN;
  const userId = process.env.IG_USER_ID;
  if (!accessToken) {
    return NextResponse.json({ items: [], error: "IG_ACCESS_TOKEN ausente" }, { status: 200 });
  }

  try {
    // Se userId existir, usa endpoint de user media, senão tenta /me
    const base = "https://graph.instagram.com";
    const id = userId ? userId : "me";
    const url = `${base}/${id}/media?fields=id,media_url,permalink&access_token=${accessToken}`;
    const res = await fetch(url, { next: { revalidate: 60 } });
    if (!res.ok) throw new Error(`Instagram API error: ${res.status}`);
    const data = await res.json();
    return NextResponse.json({ items: data.data || [] }, { status: 200 });
  } catch (e) {
    console.error(e);
    return NextResponse.json({ items: [], error: "Falha ao buscar Instagram" }, { status: 200 });
  }
}