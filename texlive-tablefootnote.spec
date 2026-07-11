%global tl_name tablefootnote
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1c
Release:	%{tl_revision}.1
Summary:	Permit footnotes in tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tablefootnote
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the command \tablefootnote to be used in a table or
sidewaystable environment, where \footnote will not work (and when using
\footnotemark and \footnotetext, and adjusting the counter as necessary,
is too much work).

